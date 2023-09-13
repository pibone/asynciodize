from distutils.core import setup
setup(
  name = 'asynciodize',         # How you named your package folder (MyLib)
  packages = ['asynciodize'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A package to wrap/decorate blocking functions for use in asyncIO',   # Give a short description about your library
  author = 'Daniel Peña Iglesias',                   # Type in your name
  author_email = 'contact@dani-pi.com',      # Type in your E-Mail
  url = 'https://github.com/pibone/asynciodize',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/pibone/asynciodize/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['asyncio', 'blocking', 'multithreading'],   # Keywords that define your package best
  install_requires=['asyncio'],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Multithreading',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.9',      #Specify which pyhton versions that you want to support
  ],
)