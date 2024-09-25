# RBF -- Radial Basis Function Visualization Heatmap

The content of this repository is intended to support the paper **“iGAiVA: Integrated Generative AI and Visual Analytics in a Machine Learning Workflow for Text Classification.”** by authors **Yuanzhe Jin**, Adrian Carrasco, and Min Chen.

Radial Basis Function (RBF) is an important concept widely used in mathematics and engineering. We apply the concept of RBF to the visualization of heatmaps, making it useful for analyzing the relationships between projected data points.

**Definition**: RBF is a class of special functions whose value depends only on the distance between the input point and a fixed point (called the center).

## Features
1. The RBF output value is the same for all points equidistant from the center.
2. RBF has a greater influence in the area close to the center, and its influence gradually decreases as the distance increases.
3. The most common RBFs include Gaussian functions and linear functions (custom functions can also be used).
4. RBF is used to create a continuous heatmap surface from discrete data points, making it easier to observe and understand the overall trends in the data.
5. ...

## Installation
Support Library:

1. sklearn
2. pandas
3. numpy
4. Catboost
5. seaborn

## Recommend
The ipynb code can also be used in Google Colab.

A UI design is proposed in the file and is a runnable program. Users can use that UI to interact with their data.

## License

RBF code was released under the Apache License 2.0. See [LICENSE](LICENSE) for additional details.

## Code Author
Yuanzhe Jin

## Citing us ٩(๑>◡<๑)۶

If you find this repository useful, please consider giving a star :star: and citation:

```
@misc{
@misc{Jin:2024:igaiva,
      title={iGAiVA: Integrated Generative AI and Visual Analytics in a Machine Learning Workflow for Text Classification}, 
      author={Yuanzhe Jin and Adrian Carrasco-Revilla and Min Chen},
      year={2024},
      eprint={2409.15848},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2409.15848}, 
}
}
```
