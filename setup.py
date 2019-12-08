from distutils.core import setup
setup(
  name = 'crypto-com-api',         # How you named your package folder (MyLib)
  packages = ['crypto-com-api'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Python Wrapper for Crypto.com API',   # Give a short description about your library
  author = 'Igor Jakovljevic',                   # Type in your name
  author_email = 'igor.jakovljevic@outlook.com',      # Type in your E-Mail
  url = 'https://github.com/IgorJakovljevic/crypto-com-api',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    
  keywords = ['Crypto-com', 'API', 'Python'],   # Keywords that define your package best
  install_requires=[           
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)