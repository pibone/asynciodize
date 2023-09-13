from distutils.core import setup
setup(
  name = 'asynciodize',
  packages = ['asynciodize'],
  version = '0.1-beta.2',
  license='MIT',
  description = 'A package to wrap/decorate blocking functions for use in asyncIO',
  author = 'Daniel Peña Iglesias',
  author_email = 'danpeis@gmail.com',
  url = 'https://github.com/pibone/asynciodize',
  download_url = 'https://github.com/pibone/asynciodize/archive/refs/tags/v0.1-beta.2.tar.gz',    
  keywords = ['asyncio', 'blocking', 'multithreading'],   
  install_requires=['asyncio'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.9',
  ],
)