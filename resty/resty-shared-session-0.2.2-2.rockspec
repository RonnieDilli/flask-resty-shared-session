package = "resty-shared-session"
version = "0.2.2-2"

source = {
  url = "git://github.com/RonnieDilli/flask-resty-shared-session.git",
  tag = "v0.2.2-2",
}

description = {
  summary = "Redis-based sessions shared between flask and openresty",
  homepage = "https://github.com/RonnieDilli/flask-resty-shared-session",
  license = "MIT",
}

dependencies = {
  "lua >= 5.1",  -- lua-nginx-module needed
  "lua-resty-cookie >= 0.1.0-1",
}

build = {
    type = "builtin",
    modules = {
        ["resty.shared_session"] = "resty/lib/resty/shared_session.lua"
    }
}
