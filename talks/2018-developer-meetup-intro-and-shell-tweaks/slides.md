## Developer meetup intro <!-- .element style="text-align: center; margin-left: 0px" -->

------

<div style="text-align: center; margin-top: 2rem; margin-bottom: 2rem">
  <img src="img/logo-developer-meetup.png" style="width: 50%"/>
</div>

Loïc Estève for the SED team  <!-- .element style="text-align: center; margin-left: 0px" -->

==

## Feed-back more than welcome!

Talk to us after the meetup!

website: https://huit.re/dev-meetup-paris

pad: https://huit.re/dev-meetup-paris-pad

mailing list: [dev-meetup-paris@inria.fr](mailto:dev-meetup-paris@inria.fr)
(click [here](https://sympa.inria.fr/sympa/subscribe/dev-meetup-paris) to
subscribe)

==

<img class="img-center" src="img/i-have-no-idea-what-i-am-doing.jpg"/>

==

<img class="img-center" src="img/i-have-some-sort-of-idea-what-i-am-doing.jpg" height="500rem"/>

==

<img class="img-center" src="img/this-could-change-my-life.jpg"/>

==

<img class="img-center" src="img/it-actually-works.jpg"/>

==

<img class="img-center" src="img/we-need-you-uncle-sam.jpg"/>

==

## Example topics

* tools you could not live without
* tricks for common tools (shell, LaTeX, git, ...) that make your life easier
* present your current pain points: get suggestions, maybe even solutions (you
  won't know if you don't try)

==

# Some shell tweaks

==

## Focus in this talk

* I have typed a similar command in the past
* I can't remember the full details 

==

## Usual suspects

* up/down arrow <!-- .element class="fragment" -->
* <!-- .element class="fragment" --> `history | grep the-part-i-remember`
* <!-- .element class="fragment" --> `Control-R/S`

==

## Tweak #1

<small>Inspiration from IPython</small>

`Control-P/N` matches the beginning

```
# ~/.inputrc content
"\C-p": history-search-backward
"\C-n": history-search-forward
```

==

## Tweak #2

One day I switched from bash to zsh

Settled on [prezto](https://github.com/sorin-ionescu/prezto) framework. Out-of the box:

* `Control-P/N` matches anywhere
* `Alt-P/N` matches the beginning

==

## Tweak #3

Very recently: autosuggestions

<small> I saw someone using xonsh and autosuggestions looked nice</small>

zprezto support: small change in my zsh config
([diff](https://github.com/lesteve/prezto/commit/5e5d534f9215263a2fb8dc1bb8e3cbd569864184))

* `Control-E` full completion
* `Alt-F/Backspace`: incremental

Find things you did not even remember typing

==

## Parting words

* tweaking is a journey: try things out and find things that work for you <!-- .element class="fragment" -->
* start with something that already exists and tweak it further <!-- .element class="fragment" -->
* tweaking can be a bottomless pit, know when to stop <!-- .element class="fragment" -->
* draw inspiration from people around you <!-- .element class="fragment" -->
* share your tweaks to learn even more <!-- .element class="fragment" -->

==

<span>
~1 hour to prepare this talk.
</span>
<span class="fragment">
Live demo would be less
</span>

<div class="fragment">
What is **your** next lightning about?

<img src="img/we-need-you-gotlib.jpg"/>
</div>
