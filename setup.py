from setuptools import setup, find_packages
import torch
from torch.utils.cpp_extension import CppExtension, CUDAExtension

ext_modules = [
    CppExtension('basis_cpu', ['cpu/basis.cpp']),
    CppExtension('weighting_cpu', ['cpu/weighting.cpp']),
]
cmdclass = {'build_ext': torch.utils.cpp_extension.BuildExtension}

if torch.cuda.is_available():
    ext_modules += [
        CUDAExtension('basis_cuda',
                      ['cuda/basis.cpp', 'cuda/basis_kernel.cu']),
        CUDAExtension('weighting_cuda',
                      ['cuda/weighting.cpp', 'cuda/weighting_kernel.cu']),
    ]

__version__ = '1.0.4'
url = 'https://github.com/rusty1s/pytorch_spline_conv'

install_requires = []
setup_requires = ['pytest-runner']
tests_require = ['pytest', 'pytest-cov']

setup(
    name='torch_spline_conv',
    version=__version__,
    description='Implementation of the Spline-Based Convolution'
    'Operator of SplineCNN in PyTorch',
    author='Matthias Fey',
    author_email='matthias.fey@tu-dortmund.de',
    url=url,
    download_url='{}/archive/{}.tar.gz'.format(url, __version__),
    keywords=[
        'pytorch', 'cnn', 'spline-cnn', 'geometric-deep-learning', 'graph',
        'mesh', 'neural-networks'
    ],
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    ext_modules=ext_modules,
    cmdclass=cmdclass,
    packages=find_packages(),
)
