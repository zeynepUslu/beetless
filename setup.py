try:
    from setuptools import setup
except ImportError:
    from .ez_setup import use_setuptools
    use_setuptools()


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

setup(
    name='beetless',
    version='0.1.0',
    description='Music collection service and app.',
    long_description=readme + '\n\n' + history,
    author='H. Turgut Uyar',
    author_email='uyar@itu.edu.tr',
    url='https://github.com/uyar/beetless',
    packages=['beetless'],
    package_dir={'beetless': 'beetless'},
    include_package_data=True,
    install_requires=[],
    license='MIT',
    zip_safe=False,
    keywords='music',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        "Operating System :: OS Independent"
    ],
    test_suite='tests',
    tests_require=['pytest']
)
