
class UserModelMixin:
    def get_full_name(self):
        return ' '.join(filter(None, [self.last_name, self.first_name]))  # noqa

    def get_fio(self):
        return ' '.join(filter(None, [self.last_name, self.first_name, self.middle_name]))  # noqa

    def get_number(self):
        return self.pk