---
title: Encyclopedia 3.A
myst:
  html_meta:
    "description lang=fr": |
      Top-level documentation for the Encyclopedia 3.A project.
html_theme.sidebar_secondary.remove: true
---

# Business model

::::::{div} full-width

:::::{grid} 2

::::{grid-item}
:columns: 8 

:::{epigraph}

I want to create a **social entreprise** that provides learning and training materials for individuals who want to make the most out of their **learning journey**. A good learning experience rely on the ability to take notes about a body of knowledge, in a hierarchical way that allow for retrival and complementation of those notes over time. Internet is full of information in various format and yet, most of us still uses pen and paper to build knowledge out of this endless source. The Open Source community has been building tools for years to help with the forever increasing technicity of this world.

This to take markdown notes. The resulting product would be a collection of websites developped, implemented and own by the individual whose purpose is to host and share their knowledge throughout their life. The method I have developped uses only open source softwares [Jupyter-Book](../../../Appendix/Help/Executable-Book/Jupyter), [Github](../../../Appendix/Help/Executable-Book/Jupyter) ...


The global aim is to achieve a paradigm schift to break free from the commercial publication system, a parasit that feed from the academic community (cf [Manifesto](../../../Projects/Manifesto)). 

:::

::::

::::{grid-item}
:columns: 4 

<div id="colour">

- ✍️ [Vincent Deguin](https://deugz.github.io/nb-profile/_build/html/intro.html )
- 🕑: 20 min <br>
- 🛠️ 08/04/2024 <br>      
- Finished: ✅  <br>   
- **Reviewed**: ❌<br>


</div>

<br>


**Plan**


- [Introduction](content:references:Business_Model_Title0)

    - Encyclopedia 3.A
    - Surrounding Projects

<br>

- [Canvas](content:references:Business_Model_Title1)

    - Desirability
    - Feasibility
    - Viability
    
<br>

- [Testing](content:references:Business_Model_Title2)

    - Critical Assumptions
    - Test types
    
<br>

- [Expenditures](content:references:Business_Model_Title3)


::::


:::::

::::::


(content:references:Business_Model_Title0)=
<h2>Introduction</h2>

<p class="emphase2"><strong>Encyclopedia 3.A</strong></p>

<br>

::::::{div} full-width

:::::{grid} 2

::::{grid-item}
:columns: 8 

:::{epigraph}

I started this project around 2022, while I was doing a PhD related to *Experimenting with the earliest stages of planet formation* at the Open University. At that time, I felt the urgency to share the outputs of my research in a more *open and interactive* fashion than classical accademic methods allowed, to promote reusability and collaboration 

:::

::::

::::{grid-item}
:columns: 4 


```{image} ../../../../_static/Logo/Encyclopedia-logo.png

```

::::


:::::

::::::


```{admonition} Birth story of the project
:class: dropdown

Early in my research, I started coding in Python. I found it very hard and counter intuitive. Hopefully, I have been advised to use Jupyter Notebook, an Integrated Development Environment (IDE) whose main feature was to combine Python with Markdown. I could now write and run some code within a text document. At first, it was a way to add comments and make the code less frightening, but very rapidly arised the opportunity to write stories, directly from the data reduction pipeline. This is a great feature for scientific communication and collaboration but how can you publish such outputs? Well, that is the realm of **JupyterBook**.   

```

<br>

<p class="emphase"><strong>Objectives</strong></p>


::::::{tab-set}

:::::{tab-item} Markdown Notebook

```{note}

Extract and link to Note


```

:::::

:::::{tab-item} Knowledge Factory

```{note}

Extract and link to Construction


```

:::::

:::::{tab-item} Publication & Collaboration 

```{note}

Extract and link to Publication


```

:::::


:::::{tab-item} Semantic Network

```{note}

Extract and link to Partage


```

:::::

::::::


<p class="emphase2"><strong>Test Projects</strong></p>


(content:references:Business_Model_Title1)=
<h2>Canvas</h2>

<br>

::::::::{div} full-width


<p class="emphase2"><strong>Desirability</strong></p>

<br>

```{image} Docs/Business_model_1.svg
:width: 100%
```

<br>
<br>


:::::::{dropdown} More info 

::::::{tab-set}

:::::{tab-item} Value Proposition

The benefits resulting from following my method can be divided in two (input and output)

::::{grid} 2

:::{grid-item-card} 
:class-header: bg-light
**Input** (Tab A - B)
^^^

- All in one
- Linkable content
- Semantic Web
- Creative
- Lifelong
- Empowering



:::

:::{grid-item-card} 
:class-header: bg-light
**Output** (Tab C - D)
^^^


:::



::::

:::::


:::::{tab-item} Tab **A**

**Markdown** is a lightweight markup language for creating formatted text using a plain-text editor. It allows you to write using an easy-to-read, easy-to-write plain text format and then **convert it to structurally valid HTML**. I came accross it during my `Python` deep dive, where I discovered that you could mix Python and Markdown using a web application called `Jupyter Notebook`. To me, that was a novice python programmer at the time, that was a game changer as I could now code in a step-by-step fashion with text cells between code cells resulting in a self explanatory program (and less frightening I must say, more in Tab B). Later I discovered that Jupyter was in fact a whole ecocystem of open source software, encompassing `Jupyter Lab`, and more importantly `Jupyter-Book`. The later is defined as a tool to: 

<br>

<p class="emphase">Build beautiful, publication-quality books and documents from computational content</p>

<br>

::::{grid} 2

:::{grid-item}
:columns: 9


Somehow that sounded like what I wanted to achieve with my PhD thesis, but after one year of use, I think the capabilities extend far beyond this restrictive scope. Indeed, the online format gives me a much broader type of inputs (video, podcasts, animations, hyperlinks ...) and have a potentially infinite depth. I can also test some new way of communicate science that have never been experimented before, finding my own style. 

<br>

**Competitors:** 
- [Notion](https://www.notion.so/fr-fr): A great note taking, web-scrapping, knowledge base software that also allow IA. It is a good software but I don't see it as being dedicated for research purposes, at least not in the way I intend to design my plateform. It is a great source of aspiration though. 
- [Obsidian](https://obsidian.md/): I need to test it but looks like there is no build option to get a web-site and only allow md files (where jupyter book also allow .ipynb (python notebook))

:::

:::{grid-item-card}
:class-header: bg-light
:columns: 3

**Links**

^^^

- [Markdown](../../../Appendix/Help/Markdown/Markdown)
<br>
- [Executable Books](../../../Appendix/Help/Executable-Book/Executable-Book)
    - [Jupyter-Book](../../../Appendix/Help/Executable-Book/Jupyter)
    - [MyST](../../../Appendix/Help/Executable-Book/MyST)
<br>    
- [How do I](../../../Projects/How_do/How_do_I) use
- [How you can](../../../Projects/How_do/How_can_you) interact

:::
::::

:::::

:::::{tab-item} Tab **B**

Science must be **reproducibile**, and there is evidence that this is not always the case (ref). This is main reason why the FAIR Principles {cite:p}`Wilkinson2016` have been put in place, in order for the data to be:
- Findable
- Accessible
- Interoperable
- Reusable

The paper based publication model is not built for that purpose and very often this is resumed by a link towards a data repository at the end of a scientific paper. However, with my publication model, I can directly link my data and softwares within my notes and this is already a great improvment. But there is also a scope to go much further than this. Indeed, I have the possibility to make my software **interactive** and directly emebed into the web page. 

::::{grid} 2

:::{grid-item}
:columns: 9

```{note}

The interactivity is a feature I tested, but it still need to be perfected

```  

:::

:::{grid-item-card}
:class-header: bg-light
:columns: 3

**Links**

^^^

- [Open Science Tools](../../../Appendix/Help/OpenScience/Open_Science)
- [Binder](../../../Appendix/Help/Binder/Binder_JB)


:::
::::



:::::

:::::{tab-item} Tab **C**

You are currently navigating on my website which is the cover (the top of the iceberg) of a much deeper self own publication plateform.  

:::::

:::::{tab-item} Tab **D**

**Competitors / Partners**:

- [SciAni](https://sciani.com/): Extremely pricey but also very qualitative work

:::::

:::::{tab-item} Customer Segment

Similarily to the value proposition, the customer segment can be divided in two, the people that would use my methodology, and the consumers of the outputs resulting from it.


:::::

:::::{tab-item} Tab **E**

Explain

:::::

:::::{tab-item} Tab **F**

Explain

:::::

:::::{tab-item} Tab **G**

Explain

:::::

::::::

:::::::

::::::::


<br>
<br>


:::::::{div} full-width

```{image} Docs/Business_model_2.svg
:width: 100%
```


<br>
<br>


::::::{dropdown} More info 

:::::{tab-set}

::::{tab-item} Tab **H**

Explain

::::

::::{tab-item} Tab **I**

Explain

::::

:::::

::::::

:::::::


<br>
<br> 



:::::::{div} full-width

<p class="emphase2"><strong>Feasibility</strong></p>

<br>

```{image} Docs/Business_model_3.svg
:width: 100%
```


<br>
<br>


::::::{dropdown} More info 

:::::{tab-set}

::::{tab-item} Tab **J**

Explain

::::

::::{tab-item} Tab **K**

Explain

::::

:::::

::::::

:::::::


<br>
<br> 


:::::::{div} full-width

```{image} Docs/Business_model_4.svg
:width: 100%
```



<br>
<br>


::::::{dropdown} More info 

:::::{tab-set}

::::{tab-item} Tab **H**

Explain

::::

::::{tab-item} Tab **I**

Explain

::::

:::::

::::::

:::::::


<br>
<br> 
 



:::::::{div} full-width

<p class="emphase2"><strong>Viability</strong></p>

<br>

```{image} Docs/Business_model_5.svg
:width: 100%
```



<br>
<br>


::::::{dropdown} More info 

:::::{tab-set}

::::{tab-item} Tab **H**

Explain

::::

::::{tab-item} Tab **I**

Explain

::::

:::::

::::::

:::::::


<br>
<br> 


::::::::{div} full-width

```{image} Docs/Business_model_6.svg
:width: 100%
```


<br>
<br>

:::::::{dropdown} **Sustainable Development Goals** - In depth development

::::::{tab-set}

:::::{tab-item} SDG **3**

::::{grid} 2

:::{grid-item}
:columns: 9

<br>
<br>

<p class="emphase">Ensure healthy lives and promote well-being for all at all ages</p>

:::

:::{grid-item}
:columns: 3

```{image} ../../../_static/SVG_files/Development_goals/Sustainable_Development_Goal_03GoodHealth.svg

```

:::

::::


::::{grid} 2

:::{grid-item-card}
:columns: 6
:class-header: bg-light

**Problems**

^^^

Most of PhD students feels stress and anxiety ... 


:::

:::{grid-item-card}
:columns: 6
:class-header: bg-light

**Solutions**

^^^

:::

::::

:::::

:::::{tab-item} SDG **4**


::::{grid} 2

:::{grid-item}
:columns: 9

<br>
<br>

<p class="emphase">Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all</p>

:::

:::{grid-item}
:columns: 3

```{image} ../../../_static/SVG_files/Development_goals/Sustainable_Development_Goal_04QualityEducation.svg

```

:::

::::

::::{grid} 2

:::{grid-item-card}
:columns: 6
:class-header: bg-light

**Problems**

^^^

Teaching conditions are very different accros the globe. 


:::

:::{grid-item-card}
:columns: 6
:class-header: bg-light

**Solutions**

^^^

Internet is accessible everywhere and ...

:::

::::


:::::

:::::{tab-item} SDG **8**

::::{grid} 2

:::{grid-item}
:columns: 9

<br>
<br>

<p class="emphase">Promote sustained, inclusive and sustainable economic growth, full and productive employment and decent work for all</p>

:::

:::{grid-item}
:columns: 3

```{image} ../../../_static/SVG_files/Development_goals/Sustainable_Development_Goal_08DecentWork.svg

```

:::

::::

::::{grid} 2

:::{grid-item-card}
:columns: 6
:class-header: bg-light

**Problems**

^^^

The current commercial publication system is far from being sustainable and inclusive. Indeed it is pushing for always more article to be published (predatory journals) and is not inclusive (paywall access).



:::

:::{grid-item-card}
:columns: 6
:class-header: bg-light

**Solutions**

^^^

Internet is accessible everywhere and ...

:::

::::



:::::

:::::{tab-item} SDG **9**

::::{grid} 2

:::{grid-item}
:columns: 9

<br>
<br>

<p class="emphase">Build resilient infrastructure, promote inclusive and sustainable industrialization and foster innovation</p>

:::

:::{grid-item}
:columns: 3

```{image} ../../../_static/SVG_files/Development_goals/Sustainable_Development_Goal_09Industry.svg

```

:::

::::


::::{grid} 2

:::{grid-item-card}
:columns: 6
:class-header: bg-light

**Problems**

^^^


:::

:::{grid-item-card}
:columns: 6
:class-header: bg-light

**Solutions**

^^^

Knowledge infrastructure

:::

::::

:::::

:::::{tab-item} SDG **10**

::::{grid} 2

:::{grid-item}
:columns: 9

<br>
<br>

<p class="emphase">Reduce inequality within and among countries</p>

:::

:::{grid-item}
:columns: 3

```{image} ../../../_static/SVG_files/Development_goals/Sustainable_Development_Goal_10ReducedInequalities.svg

```

:::

::::

::::{grid} 2

:::{grid-item-card}
:columns: 6
:class-header: bg-light

**Problems**

^^^

The fact that libraries have to pay indecent fees to get access to the scholarly litterature is the cause of a schism in access to articles between rich and poor countries.


:::

:::{grid-item-card}
:columns: 6
:class-header: bg-light

**Solutions**

^^^

I publish for free and scientist not only have access but can also participate.


:::

::::


:::::

:::::{tab-item} SDG **12**

::::{grid} 2

:::{grid-item}
:columns: 9

<br>
<br>

<p class="emphase">Ensure sustainable consumption and production patterns</p>

:::

:::{grid-item}
:columns: 3

```{image} ../../../_static/SVG_files/Development_goals/Sustainable_Development_Goal_12ResponsibleConsumption.svg

```

:::

::::

::::{grid} 2

:::{grid-item-card}
:columns: 6
:class-header: bg-light

**Problems**

^^^



:::

:::{grid-item-card}
:columns: 6
:class-header: bg-light

**Solutions**

^^^


:::

::::



:::::

:::::{tab-item} SDG **13**



::::{grid} 2

:::{grid-item}
:columns: 9

<br>
<br>

<p class="emphase">Take urgent action to combat climate change and its impacts</p>

:::

:::{grid-item}
:columns: 3

```{image} ../../../_static/SVG_files/Development_goals/Sustainable_Development_Goal_13Climate.svg

```

:::

::::

::::{grid} 2

:::{grid-item-card}
:columns: 6
:class-header: bg-light

**Problems**

^^^



:::

:::{grid-item-card}
:columns: 6
:class-header: bg-light

**Solutions**

^^^


:::

::::

:::::

:::::{tab-item} SDG **16**

::::{grid} 2

:::{grid-item}
:columns: 9

<br>
<br>

<p class="emphase">Promote peaceful and inclusive societies for sustainable development, provide access to justice for all and build effective, accountable and inclusive institutions at all levels</p>


:::

:::{grid-item}
:columns: 3

```{image} ../../../_static/SVG_files/Development_goals/Sustainable_Development_Goal_16PeaceJusticeInstitutions.svg

```

:::

::::

::::{grid} 2

:::{grid-item-card}
:columns: 6
:class-header: bg-light

**Problems**

^^^



:::

:::{grid-item-card}
:columns: 6
:class-header: bg-light

**Solutions**

^^^


:::

::::


:::::

:::::{tab-item} SDG **17**

::::{grid} 2

:::{grid-item}
:columns: 9

<br>
<br>

<p class="emphase">Strengthen the means of implementation and revitalize the Global Partnership for Sustainable Development</p>

:::

:::{grid-item}
:columns: 3

```{image} ../../../_static/SVG_files/Development_goals/Sustainable_Development_Goal_17Partnerships.svg

```

:::

::::

::::{grid} 2

:::{grid-item-card}
:columns: 6
:class-header: bg-light

**Problems**

^^^



:::

:::{grid-item-card}
:columns: 6
:class-header: bg-light

**Solutions**

^^^


:::

::::


:::::

::::::


:::::::

::::::::

(content:references:Business_Model_Title2)=
## Testing

<br>


:::::::{div} full-width

<br>
<br>


<p class="emphase2"> <strong>Test types</strong></p> 

<br>

::::::{tab-set}

:::::{tab-item} Homepage

<br>

::::{grid} 2
:::{grid-item}
:columns: 2
**Quality of evidence**<br>
&starf; &star; &star; &star; &star;
:::

:::{grid-item}
:columns: 10
<p class="emphase">Tell customers what I do, and why I am important</p>
:::
::::


::::{grid} 2

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**Hp.1**</span> **Validate the problems**

^^^

Explain the problem you are solving. Investigate if your Customer Segments actually experience and care about this problem

+++

- ![flag alt >](../../../_static/Svg_icons/Under_construction.svg) [Scientific Publication](../Scientific_Publication)


- ![flag alt >](../../../_static/Svg_icons/delete-remove-uncheck-svgrepo-com.svg) [Knowledge / Information](../Knowledge_info/Knowledge_info)


- ![flag alt >](../../../_static/Svg_icons/Under_construction.svg) [Education](../Education/Education)
:::

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**Hp.2**</span> **Validate the solution**

^^^

Explain your solution and key features to this problem. Try to keep it simple. You can test different messaging to see what moves your audience

+++

- ![flag alt >](../../../_static/Svg_icons/check-mark-button-svgrepo-com.svg) [Manifesto](../../../Projects/Manifesto)

- ![flag alt >](../../../_static/Svg_icons/Under_construction.svg)[Online Format](../../../Research/PhD/How-it-works)

- ![flag alt >](../../../_static/Svg_icons/Under_construction.svg)[Tools](../../../Research/Appendix/Help_main)

:::

::::

:::::


:::::{tab-item} Research

<br>

::::{grid} 2
:::{grid-item}
:columns: 2
**Quality of evidence**<br>
&starf; &star; &star; &star; &star;
:::

:::{grid-item}
:columns: 10
<p class="emphase">Desk based research to learn from existing materials</p>
:::
::::

::::{grid} 2

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**Re.1**</span>**Litterature Review**

^^^


:::

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**Re.2**</span> **Trend Analysis**

^^^

- ![flag alt >](../../../_static/Svg_icons/Under_construction.svg) [Open Science]()

:::

::::

<br>

::::{grid} 2

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**Re.3**</span>**Market Size / Competitor Analysis**


^^^


:::

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**Re.4**</span>**Observation**

^^^


:::

::::

:::::

:::::{tab-item} Survey

<br>

::::{grid} 2
:::{grid-item}
:columns: 2
**Quality of evidence**<br>
&starf; &starf; &star; &star; &star;
:::

:::{grid-item}
:columns: 10
<p class="emphase">Surveys are great for getting a quick overview, but have limitations (non verbal communication ...).</p>
:::
::::

::::{grid} 2

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**Su.1**</span> **Discovery Survey**

^^^


:::

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**Su.2**</span>**A/B Testing**

^^^


:::

::::

<br>

::::{grid} 2

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**Su.3**</span>**Feature Ranking**


^^^


:::

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**Su.4**</span>**Demographic Survey**

^^^


:::

::::

:::::

:::::{tab-item} Interview

<br>

::::{grid} 2
:::{grid-item}
:columns: 2
**Quality of evidence**<br>
&starf; &starf; &starf; &star; &star;
:::

:::{grid-item}
:columns: 10
<p class="emphase">Interviews are excellent to get face to face with your customers and really understand their needs and goals(listen more, talk less - ask open ended questions - ask “why” to get to the root).</p>
:::
::::

::::{grid} 2

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**In.1**</span> **Customer Interviews**

^^^


:::

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**In.2**</span>**Focus Groups**

^^^


:::

::::

<br>

::::{grid} 2

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**In.3**</span>**Talk To Partners**


^^^


:::

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**In.4**</span>**Talk To Experts**

^^^


:::

::::

:::::

:::::{tab-item} Prototype

<br>

::::{grid} 2
:::{grid-item}
:columns: 2
**Quality of evidence**<br>
&starf; &starf; &starf; &starf; &star;
:::

:::{grid-item}
:columns: 10
<p class="emphase">A prototype is a tangible expression of your idea. This can be a drawing, a website, a model or even a performance. The goal is to show your solution rather than explain it. By showing it, customers can interrogate it and provide better feedback.</p>
:::
::::

::::{grid} 2

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**Pr.1**</span> **Build A Website**

^^^


:::

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**Pr.2**</span>**Explainer Video**

^^^


:::

::::

<br>

::::{grid} 2

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**Pr.3**</span>**Clickable Wireframe**


^^^


:::

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**Pr.4**</span>**Social Media Campaign**

^^^


:::

::::

:::::

:::::{tab-item} Teach



:::::

:::::{tab-item} Collaborate



:::::

:::::{tab-item} Sell

<br>

::::{grid} 2
:::{grid-item}
:columns: 2
**Quality of evidence**<br>
&starf; &starf; &starf; &starf; &starf;
:::

:::{grid-item}
:columns: 10
<p class="emphase">The only way to truly validate your idea is to ask your customers to pay for it. It’s only when people are required to put down their cash that they have to 100% commit. Think about the simplest, cheapest thing that you can build/make/do to get a commitment of payment. </p>
:::
::::

::::{grid} 2

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**Se.1**</span> **Online Shop**

^^^


:::

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**Se.2**</span>**Pop-Up**

^^^


:::

::::

<br>

::::{grid} 2

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**Se.3**</span>**Presale**


^^^


:::

:::{grid-item-card}
:class-header: bg-light

<span style="float: right">**Se.4**</span>**Crowdfunding**

^^^


:::

::::


:::::

::::::

:::::::


(content:references:Business_Model_Title3)=
## Expenditures 

If I am successfull, I would like to buy:

- 3 domain names (for 10 years)
    - science-bf-people.org: 10 x 10 = 100 £
    - sbfp-vdeguin.com: 10 x 10 = 100 £
    - sbfp-vd-teaching.com: 10 x 10 = 100 £
- pay for my OU writing fees (to submit my thesis and pursue my accademic career):
    - 565 £
- pay a freelancer to work on a new logo
    - 50£
- print visit cards 
    - 500 cards 50£
    



# Comments 


<script src="https://utteranc.es/client.js"
        repo="Deugz/Encyclopedia-Home"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>


::::{grid} 3

:::{grid-item}
:columns: 4

:::

:::{grid-item}
:columns: 4

<script type='text/javascript' src='https://storage.ko-fi.com/cdn/widget/Widget_2.js'></script><script type='text/javascript'>kofiwidget2.init('Buy me a coffee', '#317315', 'O4O6EZO78');kofiwidget2.draw();</script> 

:::

:::{grid-item}
:columns: 4

:::

::::





