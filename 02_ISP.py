"""
Instead of one fat interface many small interfaces are preferred based on groups of methods, each one serving one submodule.
"""

class Imessage(object):

    def send_email(self,*args, **kwargs):
        raise NotImplementedError()

    def send_sms(self,*args, **kwargs):
        raise NotImplementedError()

    def send_mail(self,*args, **kwargs):
        raise NotImplementedError()

    def send_smtp(self,*args, **kwargs):
        raise NotImplementedError()
