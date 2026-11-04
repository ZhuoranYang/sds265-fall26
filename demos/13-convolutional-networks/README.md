# Lecture 13: CNN demos

Run the teaching notebooks in order, with prediction questions before each experiment
and `Try it` prompts at the end. The new companions follow Lecture 11's PyTorch,
MNIST, explicit-shape, and feature-inspection approach.

| Notebook | Classroom purpose | Compute and downloads |
|---|---|---|
| `convolutional-networks.ipynb` (existing) | Small CNN, BatchNorm train/eval behavior, feature maps | CPU; local digits CSV |
| `lenet-mnist.ipynb` | Fixed filters → LeNet-style training; compare with Lecture 11 MLP | CPU or CUDA; about 11 MB MNIST |
| `alexnet-resnet.ipynb` | Pretrained predictions, AlexNet filters, parameter counts, identity/projection shortcuts; optional Hugging Face checkpoint | CPU or CUDA; about 280 MB TorchVision weights, plus about 45 MB optional Hub checkpoint |

For a short lecture, use LeNet Sections 2–4, then AlexNet/ResNet Sections 2–4.
The LeNet default is 6,000 training images, 2,000 disjoint validation images, three
epochs per model. The larger models are explored through pretrained inference and feature inspection.
Actual runtime depends on the allocated CPU/GPU; cells print timings for training.

## Google Colab

Open either new `.ipynb` using **File → Upload notebook**. Run all cells on the default
CPU runtime, or select **Runtime → Change runtime type → T4 GPU** before running.
Both use `cuda` when available and otherwise use `cpu`.
To force CPU on a GPU runtime, assign `device = torch.device('cpu')` immediately
after the setup cell. The notebooks run directly in Colab with public data and weights.
Data, example image and public weights are downloaded on first run.
Colab provides the main packages; the optional Hugging Face cell installs `timm`
if missing. A local environment needs torch, torchvision, numpy, pandas,
matplotlib and Pillow; the optional cell also needs timm.

Open the notebooks directly in Colab:

- [LeNet in Colab](https://colab.research.google.com/github/ZhuoranYang/sds265-fall26/blob/main/demos/13-convolutional-networks/lenet-mnist.ipynb)
- [AlexNet and ResNet in Colab](https://colab.research.google.com/github/ZhuoranYang/sds265-fall26/blob/main/demos/13-convolutional-networks/alexnet-resnet.ipynb)


## Sources and changes

- **Ben Trevett**, [pytorch-image-classification](https://github.com/bentrevett/pytorch-image-classification),
  specifically `2_lenet.ipynb`, `3_alexnet.ipynb`, and `5_resnet.ipynb`.
  Reference checkout: commit `33c9cfdb9097bc65b5800c1996f199f0ba520888`.
  Copyright (c) 2018 Ben Trevett; MIT license retained in `LICENSE-bentrevett`
  and in the original checkout. We borrow the architecture progression and
  filter/feature-inspection teaching ideas. The companion code and prose are
  newly written for SDS265: small MNIST subsets, comparison to our Lecture 11
  MLP, explicit shapes, and pretrained inference replace the longer CIFAR/bird
  training and fine-tuning exercises. The upstream checkout is kept separately for reference.
- **SDS365 spring 2026**, `demos/convolution/convolve_demo.ipynb` and
  `cnn_mnist_demo.ipynb`: fixed-filter intuition and MNIST classification sequence,
  rewritten from SciPy/Keras into PyTorch. The brain-food exercise needs a much
  larger imaging download and is better suited to a project.
- **SDS265 spring 2026**: the neural-net/deep-net demos supply general neural-network
  context; the dedicated convolution material is in SDS365.
- **SDS265 Lecture 11**, `mlp-training.ipynb`: MNIST loader, pixel scaling, device
  convention, and the $784\to256\to128\to10$ MLP architecture.
- **Hugging Face / timm**,
  [ResNet-18 model card](https://huggingface.co/timm/resnet18.a1_in1k) and
  [quickstart](https://huggingface.co/docs/timm/quickstart): the optional Hub loading
  and model-specific preprocessing example is adapted from these sources.
  The checkpoint model card declares Apache-2.0. Its recipe differs from the
  TorchVision checkpoint, so this section compares separately trained checkpoints.
- **PyTorch / TorchVision**: pretrained model implementations, weights, category
  names and image preprocessing. The sample dog image comes from the
  [PyTorch Hub example](https://github.com/pytorch/hub/tree/master/images).
  [AlexNet documentation](https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.alexnet.html)
  explains that this implementation follows the later AlexNet variant.

The original reference repository is cloned locally under
`upstream/pytorch-image-classification/`. That reference checkout is ignored by the
course repository; the public demo ships the revised notebooks and license.
Recreate it with:

```bash
git clone https://github.com/bentrevett/pytorch-image-classification.git upstream/pytorch-image-classification
git -C upstream/pytorch-image-classification checkout 33c9cfdb9097bc65b5800c1996f199f0ba520888
```

## Validation

Both new notebooks were executed end-to-end on local CPU with PyTorch 2.10.0
and TorchVision 0.25.0, including real MNIST training, pretrained inference,
residual-block equality checks, intermediate tensor traces, and the optional
Hugging Face checkpoint. Saved notebook outputs show these runs. Training and
validation curves and feature visualizations were rendered for inspection.
The Mac required its system trust certificates for the Hub download; this was
configured only in the validation process, without disabling TLS verification.
Hosted Google Colab and CUDA execution have not been directly tested here.

Edit the notebooks directly. The older `build_notebook.py` predates the expanded teaching prose.
