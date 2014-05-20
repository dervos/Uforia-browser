# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
from pyes.tests import ESTestCase, get_conn
import six
if six.PY2:
    from io import StringIO
else:
    from io import BytesIO as StringIO

class DumpCurlTestCase(ESTestCase):
    def setUp(self):
        super(DumpCurlTestCase, self).setUp()

    def testDumpCurl(self):
        """Test errors thrown when creating or deleting indices.

        """
        dump = StringIO()
        conn = get_conn(dump_curl=dump)
        result = conn.index(dict(title="Hi"), self.index_name, self.document_type)
        self.assertTrue('ok' in result)
        self.assertTrue('error' not in result)
        dump = dump.getvalue().decode("utf-8")
        self.assertTrue("""
            curl -XPOST 'http://127.0.0.1:9200/test-index/test-type?pretty=true' -d '{"title": "Hi"}'
            """.strip() in dump)

if __name__ == "__main__":
    unittest.main()
