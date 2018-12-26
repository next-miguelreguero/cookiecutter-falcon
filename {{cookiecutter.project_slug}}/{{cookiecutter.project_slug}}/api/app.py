import falcon
from .resources import *

application = falcon.API()

extra_handlers = falcon.media.Handlers({
    'application/msgpack': falcon.media.MessagePackHandler(),
})

application.req_options.media_handlers.update(extra_handlers)
application.resp_options.media_handlers.update(extra_handlers)
