# DNC - Events API Exercise

## General

Provided is a codebase in-development for an API with several endpoints that return JSON. It's based on a sqlite3 database (`data.db`) pre-loaded with data, with two tables, `events` and `locations`.

The API runs in a [Flask](https://flask.palletsprojects.com/) (Python web framework) application. Included `Pipfile` contains all dependencies.

---

## Your Tasks

### Overall

* Provide a review for some code in the app (see instructions below) - **Task 1**
* Add a new feature to the app (see instructions below) - **Task 2**
* Update the README with any documentation / explanation as needed
* Make sure we can understand what we need to do to run the app/test out your work
* .zip up all the files for your app + your markdown code review, and submit that back to the DNC (following instructions you received)

**A few notes:**
* Please spend no more than ~3 hours on this -- if you run out of time, just make clear in the README what you would do next!
* If you haven't used Python much before, that's OK. We don't expect you to be an expert in a couple hours, we just want to learn about your approach to these tasks.
* If you have any trouble getting set up or if anything is unclear, please reach out to your contact at DNC. We don't intend there to be any trick questions or deliberate confusion here, and we want you to be able to show us a bit of what you can do.

### What we're looking for

* Constructive communication about your and others' code
* Ability to get a sense of code that's new to you
* Evidence that you write code that works
* Ability to work with an existing app + real-life data

---

### **TASK 1**: Review some code and fix some bugs

We've provided some code that contains:
* A base working app with API endpoints, as described
* A couple new additions to the app, which you can find by searching for the comment `NEW ADDITION PROPOSED`

Assume that all code marked by `NEW ADDITION PROPOSED` has recently been added to create a new way of listing out and viewing details about events. (In 'real life', we use GitHub and review each other's pull requests.) The code was written to fulfill the following goals:
* Add an initial event detail page to the Flask app that shows useful information about each event.
* Add a page to the app that will list events based on state at url `/event-list/<STATE>`, e.g. `/event-list/NY` should list all the events in New York.

**Please add to the file `review.md` (Markdown file) your review of the newly added code, the way you might review these additions for a colleague. You can assume someone else has added this code and asked you for your review.**

* We know there are bugs in the code that is newly added -- please identify them in your `.md` review of the code, _and_ actually fix the bugs in the code so all elements of the app will run successfully!
* Knowing the goal that this code was meant to fulfill, feel free to comment on any other element of the code that is newly added. Do you have suggestions? We're not looking for anything in particular here. We genuinely want to know what you think.


### **TASK 2**: Add a new feature

Once the bugs are fixed and the app will run,

**We need to add a way to attend/RSVP to an event.**

You can implement this however you want. You can change or add to (or remove!) any provided code that you want. You can also modify database schemas or add dependencies if you like (but you're not required to). You do not need to add a front end (but you can).

Just make sure that you add to the README below so we can easily understand how to use what you've added. Feel free to add any explanatory comments that will help us understand your assumptions.

---

## Understanding the app

### Requirements

You will need to have Python 3.8 and `pip` installed (reach out to your contact at DNC if you have any trouble installing these).

### Installation

To install, run the following:

```
pip install pipenv
pipenv install
```

Pipenv is a tool that provides a contained development environment.

### Running the server

If you're not already in the virtual environment, run `pipenv shell`

Run `flask run` to start the webserver.

The API will be live at `http://127.0.0.1:5000/`.

## Endpoints

### `/api/events` (`GET`)

List all events.

#### Sample request

`curl http://localhost:5000/api/events/`

### `/api/events/<id>` (`GET`)

List individual event detail by ID.

#### Sample request

`curl http://localhost:5000/api/events/7/`

## Additional documentation (feel free to edit)

TODO add

