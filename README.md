# next.filmfest.by

[![Travis](https://img.shields.io/travis/kinaklub/next.filmfest.by/master.svg)](https://travis-ci.org/kinaklub/next.filmfest.by)
[![AppVeyor](https://img.shields.io/appveyor/ci/nott/next-filmfest-by/master.svg)](https://ci.appveyor.com/project/nott/next-filmfest-by/history)
[![Netlify static preview](https://img.shields.io/badge/preview-ready-brightgreen.svg)](https://filmfest.netlify.com/)

Welcome to the workplace for upcoming website for Cinema Perpetuum
Mobile short film festival. Our goal is to gracefully replace
[the existing version](http://filmfest.by) with new code feature by
feature.

Join our chat https://riot.im/app/#/room/#cpm-dev:matrix.org for
questions.

The goal of new website version is to create a user-friendly admin
panel for festival volunteers. The feature set is taken from the
experience we've gathered during previous festivals.

## How to join development and be a part of CPM movement

We welcome all contributors and enhancements that help to make this
tool for festival to be awesome. Feel free to jump in and help with
things to your liking.

Your freedom is your creativity - being it good design, some bits
of code, or another contribution that helps to push the movement.
Making a film festival together is a great thing on its own, but to
make it worth your time even more we've choosen `UNLICENSE` to make
sure that you can reuse the bits we've created together without
restrictions and limitations - being it your commercial projects or
open source. If you wanted to learn about programming or creating
websites to get a job - that might be your chance.

For experienced, the most straightforward areas to contribute are:

* backend written in Django / Wagtail
* frontend - a lot can be done here
* design / styling
* data migration (organize data related to previous festivals in JSON)

### Communication

* Chat - https://riot.im/app/#/room/#cpm-dev:matrix.org
* Board of Chaos- https://trello.com/b/6S00yyl1/next-filmfest-by-public
* Meeting Follow Ups (notes, sources for Trello)
  - https://github.com/kinaklub/docs/blob/master/MFU_2016_07_19_filmfest.by.md
  - https://github.com/kinaklub/docs/blob/master/MFU_2016_07_21_filmfest.by.md

## Technology stack

```
Programming:
- Wagtail
  - Django
    - Python
      - pip/tox/virtualenv
    - HTML5/CSS
    - JavaScript

Deployment:
- Docker Compose
  - Docker
    - Digital Ocean
      - SSH
      - HAProxy
      - PostgreSQL
      - Elasticsearch
```

## Development process

We use [github](https://github.com) for development. In order to start
one needs to fork and clone the repository:

1. fork
   [kinaklub/next.filmfest.by](https://github.com/kinaklub/next.filmfest.by)
   using github UI

2. clone forked repository to one's local machine:

    ```
    git clone git@github.com:yourusername/next.filmfest.by.git
    ```

3. add upstream repository as a remote:

    ```
    git remote add upstream git@github.com:kinaklub/next.filmfest.by.git
    ```

Before starting working on next improvement one usually does the
following:

1. switch to local `master`:

    ```
    git checkout master
    ```

2. pull recent changes from `upstream` `master`:

    ```
    git pull upstream master
    ```

3. create a new feature branch:

    ```
    git checkout -b branch_name
    ```

4. create corresponding branch in one's fork:

    ```
    git push -u origin branch_name
    ```

After commiting everything to the feature branch one usually does the
following:

1. push the changes to one's fork:

    ```
    git push
    ```
    
2. create a pull request using
   [github UI](https://github.com/kinaklub/next.filmfest.by/compare).
   
PR review process:

1. we use [Travis CI](https://travis-ci.org) for launching tests on PRs

2. we don't merge PRs to master until tests are green

3. we require the PRs to be reviewed by at least one team member

4. reviewer adds comment "LGTM" when one think the PR is good to be merged

5. PRs are usually merged by the authors


## Development environment

1. Install [Docker](https://docs.docker.com/) and [docker-compose](https://docs.docker.com/compose/)

2. Don't forget to set DOCKER_HOST environmental variable or add yourself to group `docker`

3. Start web contatiner:

    ```
    docker-compose up web
    ```

4. Give postgres 20-30 seconds to initialize

4. Create a local user:

    ```
    docker-compose run web createsuperuser
    ```

5. Visit http://127.0.0.1:8000/ in your web browser

### Recreating development environment

If one wants to recreate their development environment from scratch
and one doesn't care about the existing data in database, one needs to:

1. stop all the containers:

    ```
    docker-compose stop
    ```

2. remove containers

    ```
    docker-compose rm -r
    ```

3. rebuild images

    ```
    docker-compose build
    ```

4. use quickstart guide above for setting up the development environment

### Testing code

The command below is usually enough for local testing:

 ```
 docker-compose run web test
 ```

If Python dependencies have changed recently, one might need to add
paramter `-r` once:

 ```
 docker-compose run web test -r
 ```
