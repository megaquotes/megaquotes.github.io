---
layout: default
title: Quotes
permalink: /blog/
nav_order: 3
---

# Blog

Welcome to my blog! Here are all my posts:

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date: "%B %d, %Y" }}
    </li>
  {% endfor %}
</ul>

