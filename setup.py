from setuptools import setup

setup(name='apiaiWebhookSerializer',
      version='0.1.0',
      description='Serialize Api.ai Webhook requests and responses to a proper python object',
      url='https://github.com/dusterherz/apiai-python-webhook-serializer',
      author='Aude Lejuez',
      author_email='audelejuez@gmail.com',
      license='MIT',
      install_requires=[
          'addict',
      ],
      packages=['apiaiWebhookSerializer'],
      zip_safe=False)
