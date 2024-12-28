---
layout: default
title: Quotes
permalink: /quotes/
nav_order: 3
---

# Quotes


<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date: "%B %d, %Y" }}
    </li>
  {% endfor %}
</ul>

