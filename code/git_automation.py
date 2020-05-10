#!/usr/bin/env python

from git import Repo
import os

'''Under construction python git-automation'''

git_repo=Repo(os.getcwd())
git_repo.git.add('example.txt')

repo.git.commit(m='test msg')
git_repo.git.push()

git_repo.git.status()
print(git_repo.git.status())