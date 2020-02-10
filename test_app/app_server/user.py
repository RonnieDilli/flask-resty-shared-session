from .errors import UserNotFound, BadPassword, LoginError, Unauthorized

USER_FIXTURES = (
    {'email': 'joe@gmail.com', 'password': 'itsjoe', 'groups': ('one', 'three'), 'roles': ('admin', 'editor')},
    {'email': 'sam@gmail.com', 'password': 'itssam', 'groups': ('two',), 'roles': ('viewer',)},
    {'email': 'esteban@gmail.com', 'password': 'itsesteban', 'groups': ('one', 'four'), 'roles': ('admin', 'publisher')},
    {'email': 'maria@gmail.com', 'password': 'itsmaria', 'groups': tuple(), 'groups': tuple()}
)

USER_FIXTURES_BY_EMAIL = {u['email']: u for u in USER_FIXTURES}

class User(object):
    def __init__(self, email, password, groups=None, roles=None):
        self.email = email
        self.password = password
        self.groups = set(list(groups or []))
        self.roles = set(list(roles or []))

    @classmethod
    def by_email(cls, email):
        user_data = USER_FIXTURES_BY_EMAIL.get(email)
        if user_data is None:
            raise UserNotFound(email)
        assert user_data['email'] == email
        return cls(
            email=user_data['email'],
            password=user_data['password'],
            groups=user_data['groups'],
            roles=user_data['roles']
        )

    def check_password(self, pw):
        if pw != self.password:
            raise BadPassword()

    @classmethod
    def attempt_login(cls, email, password):
        try:
            user = cls.by_email(email)
            user.check_password(password)
            return user
        except (UserNotFound, BadPassword):
            raise LoginError(email)

    def is_group_member(self, group):
        return group in self.groups

    def verify_group_access(self, group):
        if not self.is_group_member(group):
            raise Unauthorized("Not a member of group '%s'" % group)

    def is_role_member(self, role):
        return role in self.roles

    def verify_role_access(self, role):
        if not self.is_role_member(role):
            raise Unauthorized("Not a member of role '%s'" % role)
