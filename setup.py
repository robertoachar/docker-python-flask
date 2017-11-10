from setuptools import setup

setup(name='docker_python_flask',
      version='1.0.0',
      description='A playground for Docker with Python and Flask.',
      author='Roberto Achar',
      author_email='robertoachar@gmail.com',
      packages=['docker_python_flask'],
      entry_points={
          'console_scripts': [
              'docker_python_flask=docker_python_flask.__main__:main'
          ]
      },
      license='MIT')
