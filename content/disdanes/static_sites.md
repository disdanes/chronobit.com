Title: Static Site Generators
Date: 2016-02-09 22:05
Tags: web development
Slug: disdanes/static-site-generators
Authors: Justin Lindsey
Summary: There are an incredible number of static site generators out in the wild. I tried many and landed on one that I think I like.
no_title: True

### What is a static site ?

The whole idea behind a static site is that we want to live like it's 1995. We're a bunch of internet hating greybeards who don't like any new things, and want to use a command line prompt to type a website.

Alright, so that's not entirely true. If anything, the return to earlier times is a way to simplify all the complexities of a web stack. A static site is just .html files, with some .css and .js thrown in for good measure. There is no *server*, no database, no security patches to worry about, no SSL to configure, and that helps reduce the overhead of managing a website. 

I've tried self-hosting wordpress, and I can attest to all the problems that come with updating security patches, manging apache/mysql memory usage so the server doesn't kill the database, restarting the server when it crashes, and providing a nice sub three second loadtime for all of folks who would like to view the content. Don't get me wrong, Wordpress is really nice to use from a content author's perspective, it's just a headache to maintain.

<div class="col-md-6" markdown="1">
![Bread Cat](/theme/images/disdanes/bread_cat.png)
</div>

### Static Site Generators

Static site generators are basically frameworks that help you enforce MVC-lite by keeping your content, styling, and templates all seperate. Most of them involve creating templates for your site/blog, then writing the content in a markup language like Markdown or reStructuredText, then publishing it to a host like Github Pages, Amazon S3, or a server of your choosing.

I tried to compare static site generators for the experience of creating a site, authoring the content, and ease of deploying the generated html to a hosting service like Amazon. 

### [Harp](http://harpjs.com/)
Harp is the first static site generator that I spent some time with creating the initial Chronobit.com website. I borrowed the [Helios theme](http://html5up.net/helios) from html5up.net, and used that as the css/js basis for creating the site. Harp puts you directly into the html, and lets you write Jade or EJS templates for creating your content. I really liked the simplicity of jade templates, but after reviewing the initial templates I created a couple years ago, I realize that I would need to re-look up the definition of the Jade syntax, and it would probably just be easier to do html, or some other markup language for managing the content. I also remember needing to manually copy my static files onto S3. At this point I really want a push button solution for doing that, so s3cmd/awscli would probably be the best avenue for publishing content. 

* Author Experience: Text Editor of your choice + Jade/EJS/HTML templates
* Ease of Deploy: Easy-Medium. Compile + copy files to S3.
* Support: Some nice features added since I last used it, looks like there is still development progress.
* Cons: Harp kind of forces you to keep content inside of the templates, which i'm not a fan of.

### [Hugo](https://gohugo.io/)
Hugo looks promising, and I really like the speed they’ve shown compiling a huge amount of content for a static site. Their documentation looks really good, but when I pulled in a theme, and tried to build my site the outputted html wasn't themed properly. Started to dig into Hugo a bit more, but I'm not the least bit familiar with Go.

### [Ghost](https://ghost.org/) + [Buster](https://github.com/axitkhurana/buster)
I really, really love the Ghost editor for authoring content. It’s probably my favorite splitscreen markdown editor. I was trying to evaluate what the work would be to edit the Ghost templates, and then export the site with buster to static files. Buster is a python script that basically calls wget recursively to download all of your pages into a folder that can then be shipped to Github pages/S3/anywhere. The pages are generated with the url that is specified in your configuration file, so the generated files will only work once pushed to their final destination (and the url resolves). The greatest strength of Ghost which is it’s blog first approach, is also it’s greatest weakness. The theming is setup around a blog, and so there really isn’t an easy to expose additional pages that aren’t quite blog content. Thinking about having 1 off pages that aren’t necessarily a blog means I’d have to step outside of ghost and manually craft them. I was experimenting a bit with the buster approach, but if you use resources that aren't linked on the site (I was trying to load a 3D model with three.js) then it won't get included in buster's generate, and you'll have to manually grab that file as apart of your upload.

* Author Experience: Custom markdown editor, nice UI for viewing posts
* Ease of Deploy: Lots of steps. Build posts, run buster to export them, then copy files to S3.
* Support: Organizational backing, but nobody is focusing on using Ghost to build static sites. Apps/plugin support still in the future.
* Cons: No native support for static site compilation.

### [Cactus](http://cactusformac.com/)
Cactus almost looked like a home run for what I was looking for. It leverages django templates (which I’ve got good experience with) and has a push button deploy to amazon s3 all rolled in. The only problem is that it’s largely an abandoned product. The core was open sourced which is awesome, but it doesn’t look like it has gotten any traction, which is really unfortunate. The core content has to be created in a django template, as opposed to a seperate markdown file, which could be kind of a pain for migrating content in the future.

* Author Experience: Text Editor of Choice + Django Templates
* Ease of Deploy: Push Button
* Support: PR’s aren’t being pulled in, largely abandoned.

### [Pelican](http://blog.getpelican.com/)
Pelican ended up being the static site generator that I went with. It uses Jinja2 templates which are very similar to django templates, but have additional functionality. A nice part of pelican is the quickstart, decent theme support, and it's an open source python project. Supports both a blog + static site approach with some modification.

* Author Experience: Text Editor of Choice + Jinja Templates + Markdown/rst
* Easy of Deploy: Makefile ~ push button-ish
* Support: Signs of life, but some nice PR's are being ignored.
* Cons: Documentation could be better organized

### Why I didn’t try Jekyll/etc

I have nothing against Ruby, it’s a fine language and might be worth the time someday to relearn (I did some Ruby in college). After evaluating a bunch of frameworks, I figured I really needed to just pick one.

In my next post I'll go over the Pelican setup, and some fun things I ran into while trying to structure the site.
