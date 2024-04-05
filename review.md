# Your Code Review

## `app/routes.py`

### Line 12:
- `.filter_by` should be called here instead of `.filter`
- There is an extra '=' in `.filter` invocation.
###### SHOULD BE:
`.filter_by(locations.state=state)`

### Line 13:
- `events_to_list` is not used, could be removed.

### Line 18:
- You cannot call `.first` on `.query` directly. Need to add a `.filter_by` statement.
- There is an extra '=' in `.filter` invocation.
###### SHOULD BE:
`events.query.filter_by(id=id).first()`

### Line 19:
- `render_template` doesn't accept a `event_shown` parameter, correct parameter name is `event`
- There is no space between the `template_name` and `event_shown` parameters. Might want to add one to keep consistent with code base.
###### SHOULD BE:
`render_template('event.html', event=event)`

### Line 10 & 16:
- Some browsers add a '/' to the end of the URL. Might want to add it to path pattern to catch those cases.