from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from collections import OrderedDict

class LimitSetPagination(LimitOffsetPagination):
    page_size = 10
    default_limit = 10

    def get_paginated_response(self, data):
        total_pages = int(self.count / self.limit) + 1
        current_page = int(self.offset / self.limit) + 1

        return Response(OrderedDict([
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('total_pages', total_pages),
            ('current_page', current_page),
            ('results', data)
        ]))