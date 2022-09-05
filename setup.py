from distutils.core import setup

setup(
    name='MODNet',
    version='0.0.1',
    packages=['src', 'src.models', 'src.models.backbones', 'demo',
              'demo.image_matting', 'demo.image_matting.colab', 'onnx',
              'torchscript'],
    url='',
    license='',
    author='ann',
    author_email='',
    description='MODNet arranged for ann'
)
