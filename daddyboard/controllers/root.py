from pecan import expose, abort
from enum import Enum


class DaddyState(Enum):
    AVAILABLE = 1
    QUIET_PLEASE = 2
    DO_NOT_DISTURB = 3

    def __json__(self):
        return dict(
            state=self.name
        )


class RootController(object):
    state = DaddyState.AVAILABLE

    @expose('json')
    def index(self):
        return dict(
            status=self.state
        )

    @expose(template='view.html')
    def view(self):
        return dict()

    @expose()
    def set_state(self, state):
        try:
            self.state = getattr(DaddyState, state)
        except AttributeError:
            abort(400, 'Invalid State: ' + str(state))

    @expose()
    def is_state(self, state):
        if self.state == getattr(DaddyState, state, None):
            return '1'
        return '0'
