# The Necessary Library

# Before RBF
class_name = # your category list
data = # your dataset
labels = # your dataset's labels
dimension = # the number of your PCA dimensions
X_embedded = # PCA dimensions
resolution = 100 # Hyperparameter for the images

# Load Specific Model
model = CatBoostClassifier()
model.load_model('your model path')

# predict results as benchmark
prediction = model.predict(data_topic[["text", "area_TEIS"]])
prediction_flat = prediction.reshape(-1)
data['prediction'] = prediction_flat

# prediction results
data['consistent'] = data_topic['topic_name'] == data['prediction']

# Add noise to aviod singular matrix
def add_noise(data, noise_level=1e-8):
    np.random.seed(22)
    noise = np.random.normal(0, noise_level, size=data.shape)
    return data + noise

# Define customed RBF functions
def custom_rbf(r):
    return r**0.125

# For generating the RBF pool
for target_syn in class_names:

  X_train, X_test, Y_train, Y_test = train_test_split(data, labels, test_size = 0.2,random_state = 42)

  # color settings (blue -- correct, red -- incorrect)
  condition_blue = (data['topic_name'] == target_syn) & (data['consistent'] == True)
  condition_red = (data['topic_name'] == target_syn) & (data['consistent'] == False)

  data.loc[condition_blue, 'class_colored'] = 'Correct'
  data.loc[condition_red, 'class_colored'] = 'Incorrect'

  # draw dimension combinations
  for i in range(dimension):
    
    for j in range(i, dimension, gap):
      # change into dataframe
      df = pd.DataFrame({'Dimension '+str(i): X_embedded[:, i], 'Dimension '+str(j): X_embedded[:, j], 'class_colored': data['class_colored'], 'topic':data['topic_name']})
      df['training_testing'] = 'testing'
      df.loc[X_train.index, 'training_testing'] = 'training'
      df_testing = df[df['training_testing'] == 'testing']

      # letter to number mapping
      categories = {'Other': 0, 'Correct': 100, 'Incorrect': -100}

      # from text to numbers
      df_testing['code'] = df_testing['class_colored'].map(categories)
      df['code'] = df['class_colored'].map(categories)

      # select target class pixels
      df_testing_rbf = df_testing[df_testing['topic'] == target_syn]

      x_raw = add_noise(df_testing_rbf['Dimension '+str(i)])
      y_raw = add_noise(df_testing_rbf['Dimension '+str(j)])
      z_filtered = df_testing_rbf['code']

      # Set range for pictures
      x_min, x_max = x_raw.min(), x_raw.max()
      y_min, y_max = y_raw.min(), y_raw.max()

      # ============== RBF Part ======================
      rbf = Rbf(x_raw, y_raw, z_filtered, function = custom_rbf)

      x_grid, y_grid = np.meshgrid(np.linspace(x_min,x_max, resolution), np.linspace(y_min,y_max, resolution))
      z_grid = rbf(x_grid, y_grid)

      # figure for drawing
      plt.figure(figsize=(4, 4), dpi = 200)

      # colormap settings
      seismic_reversed = plt.cm.get_cmap('seismic')
      cmap_lightened = mcolors.LinearSegmentedColormap.from_list("LightenedSeismic", seismic_reversed(np.linspace(0.36, 0.64, 256)))
      seismic_reversed = cmap_lightened.reversed()

      # Heatmap
      plt.imshow(z_grid, extent = (x_min,x_max,y_min,y_max), origin = 'lower', cmap = seismic_reversed, vmin = -100, vmax = 100)
      palette = ['#a50f15','#08519c']
      scatter = sns.scatterplot(x=x_raw , y=y_raw , hue=z_filtered, palette=palette, alpha = 0.7, s = 10, legend=False)

      # label of the axis
      plt.xlabel('Dimension ' + str(i), fontsize=6)
      plt.ylabel('Dimension ' + str(j), fontsize=6)

      data_name = # name of the image
      path = # path to the folder
      # save images
      plt.savefig(path, dpi=200)
