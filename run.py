#!/usr/bin/env python

from tbviewer import app
from dotenv import load_dotenv
import os
envf = 'tbviewer/.env'  # adjust as appropriate
load_dotenv(envf)


if __name__ == '__main__':
    app.run(debug=True)
