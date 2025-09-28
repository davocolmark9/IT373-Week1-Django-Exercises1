REFLECTION

Setting up my development environment was a learning experience with both small
and big challenges. At first, I struggled with making sure I was using the right
Python version. My computer was still using an older version, so I had to
download and install the latest one before creating the virtual environment.
After that, I faced another issue with activating the virtual environment
because the commands are not the same on Windows and Linux. I fixed this by
reading the powerpoint that you've uploaded in the google classroom and testing
using `which python` and `pip list` until I saw that it worked properly.

When it came to Django, the process was easier but I still made mistakes. The
first time, I forgot to activate the venv, which caused Django to install
globally instead of inside the environment. After reinstalling correctly,
`django-admin startproject` and `runserver` worked without problems. Finally, I
had some trouble connecting my local files to GitHub. I had to carefully set the
remote URL and then test it with `git push -u origin main`. Solving these issues
step by step gave me more confidence and taught me the importance of being
patient and careful with setup. Now I feel better prepared for future projects.