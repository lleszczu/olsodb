try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name="olsodb",
      packages=["olsodb"],
      version="0.1",
      description="blah",
      author="foo",
      author_email="bar",
      url="https://github.com/gryf/olsodb",
      download_url="https://github.com/gryf/olsodb",
      keywords=["oslo.db"],
      install_requires=["oslo.db"],
      classifiers=["Programming Language :: Python :: 2",
                   "Development Status :: 5 - Alpha",
                   "Environment :: Console",
                   "Intended Audience :: End Users/Desktop",
                   "License :: OSI Approved :: BSD License",
                   "Operating System :: OS Independent",
                   "Topic :: Database :: Front-Ends"])
