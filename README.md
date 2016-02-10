Chronobit.com website is made with a static site generator [Pelican](http://blog.getpelican.com/).

There are a couple hacks that I used to try and make the website have distinct sub-sites. One of those is using Jinja's 'with' statement to filter articles by category, and then placing the articles in respective folders to their subsites.

I spam 

```
    ./bin/compile
```

for development, and then use pelican's provided develop_server.sh script to look at it locally.

## Push to Amazon S3

Assuming the amazon credentials are setup for [s3cmd](https://github.com/s3tools/s3cmd)

```
    make s3_upload
```

