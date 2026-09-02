---
layout: default
title: "S&DS 265: Introductory Machine Learning"
---

## The course

This course is designed for undergraduates and graduate students who want to
understand how modern machine learning works, and to be able to build and
evaluate these methods themselves. It is an introductory course: the goal is to
introduce the basic ideas of machine learning, and to develop each of them far
enough that you can implement it, apply it, and see where it fails.

The course covers linear regression and classification, optimization, neural
networks, unsupervised learning and latent-variable models, generative models
including diffusion, reinforcement learning, and language models.

The course is intended for students in Statistics & Data Science, Computer
Science, Engineering, and the quantitative sciences, and is useful to graduate
students in Economics, SOM, and the Sciences who expect to use these methods in
their own research. It is suitable for undergraduates with the appropriate
prerequisites, which are linear algebra, multivariate calculus, probability, and
programming experience in Python.

<div class="note">
  <p><b>Computing.</b> Every notebook runs in
  <a href="https://colab.research.google.com">Google Colab</a> in the browser —
  no local installation, no environment to configure. Click the
  <img src="{{ '/assets/colab.svg' | relative_url }}" width="34" alt="Colab" style="vertical-align:-7px">
  icon next to any demo below. Notebooks load their data over the network, so
  a fresh Colab session has everything it needs.</p>
</div>

<div class="note">
  <p><b>Meetings.</b> Monday and Wednesday, 1:05&ndash;2:30 pm, Davies
  Auditorium, 15 Prospect Street.
  Classes begin Wednesday, September 2 and end Friday, December 11.
  September 4 runs on a Monday schedule. There is no class on Labor Day
  (September 7), during October recess (October 21–25), or during November
  recess (November 21–29).</p>
</div>

The [Canvas site]({{ site.canvas_url }}) has the syllabus, announcements,
grades, and assignment submission. This page is the calendar: slides, lecture
notes, and runnable demos for each meeting.

<h2 id="calendar">Calendar</h2>

<div class="calendar-wrap">
<table class="calendar">
  <thead>
    <tr>
      <th>Date</th>
      <th>Topic</th>
      <th>Demos</th>
      <th>Slides</th>
      <th>Lecture&nbsp;Notes</th>
    </tr>
  </thead>
  <tbody>
  {%- for m in site.data.schedule %}
    <tr{% if m.topic contains "Midterm" %} class="exam"{% endif %}>
      <td class="when"><b>{{ m.date }}</b><br>{{ m.day }}</td>
      <td class="topic">{{ m.topic }}</td>
      <td>
        {%- for d in m.demos %}
        <a class="demo" href="{{ site.colab_base }}/demos/{{ d.path }}"><img
          src="{{ '/assets/colab.svg' | relative_url }}" width="34" alt="Open in Colab">{{ d.label }}</a>
        {%- endfor %}
      </td>
      <td>
        {%- if m.slides %}
        <a class="filelink" target="_blank" rel="noopener"
           href="{{ site.raw_base }}/lectures/{{ m.slides }}.pdf"><img
          src="{{ '/assets/pdf.svg' | relative_url }}" width="22" alt="">Slides</a>
        {%- endif %}
      </td>
      <td>
        {%- if m.notes %}{%- if site.notes_base %}
        <a class="filelink" target="_blank" rel="noopener"
           href="{{ site.notes_base }}/{{ m.notes }}.html"><img
          src="{{ '/assets/notes.svg' | relative_url }}" width="22" alt="">Notes</a>
        {%- endif %}{%- endif %}
      </td>
    </tr>
    {%- if m.date == "Oct 19" %}
    <tr class="recess"><td class="when">Oct 21–25</td><td colspan="4">October recess — no class</td></tr>
    {%- endif %}
    {%- if m.date == "Nov 18" %}
    <tr class="recess"><td class="when">Nov 21–29</td><td colspan="4">November recess — no class</td></tr>
    {%- endif %}
  {%- endfor %}
  </tbody>
</table>
</div>

## Readings & Textbooks

The lecture slides and notebooks are self-contained. Three textbooks are
recommended for a second explanation and additional depth, and all three are
free online. Each lecture names its own reading on the closing slide, cited by
chapter using these tags.

- **[ISLP]** *An Introduction to Statistical Learning with Applications in
  Python* — James, Witten, Hastie, Tibshirani, and Taylor.
  <a href="https://www.statlearning.com/">statlearning.com</a>
- **[D2L]** *Dive into Deep Learning* — Zhang, Lipton, Li, and Smola. The
  reference for the computational material.
  <a href="https://d2l.ai/">d2l.ai</a>
- **[DL]** *Deep Learning* — Goodfellow, Bengio, and Courville. Background and
  depth for the neural-network half.
  <a href="https://www.deeplearningbook.org/">deeplearningbook.org</a>


## Materials

Slides, notebooks, and data can be found in the following GitHub repo:
[{{ site.course_repo }}](https://github.com/{{ site.course_repo }}).
