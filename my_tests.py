import unittest
import solution as s


class TestExtractType(unittest.TestCase):
    def setUp(self):
        self.data = [('a', 1), ([], 4), ('i', 1), (0.3, 100),
                     (set(), 5), ('z', 2), ({}, 1), ('z', 3),
                     ([1, 2], 2), ({'a': 2}, 2),
                     ([3, 4], 3), ((1, 2), 2), ((3, 4), 3),
                     ((), 3), (True, 2), (False, 2), ({1, 2}, 3)]

    def test_extract_type_with_string(self):
        self.assertEqual(s.extract_type(self.data, str), 'aizzzzz')

    def test_extract_type_with_tuple(self):
        self.assertEqual(s.extract_type(self.data, tuple),
                         '(1, 2)(1, 2)(3, 4)(3, 4)(3, 4)()()()')

    def test_extract_type_with_list(self):
        self.assertEqual(s.extract_type(self.data, list),
                         '[][][][][1, 2][1, 2][3, 4][3, 4][3, 4]')

    def test_extract_type_with_set(self):
        self.assertEqual(s.extract_type(self.data, set),
                         'set()set()set()set()set(){1, 2}{1, 2}{1, 2}')

    def test_extract_type_with_dict(self):
        self.assertEqual(s.extract_type(self.data, dict),
                         "{}{'a': 2}{'a': 2}")

    def test_extract_type_with_bool(self):
        self.assertEqual(s.extract_type(self.data, bool),
                         'TrueTrueFalseFalse')


class TestReversedDict(unittest.TestCase):
    def setUp(self):
        self.data = {
            'Sofia': 'Bulgaria',
            'New York': 'USA',
            'Berlin': 'Germany',
            'London': 'Great Britain',
            'Plovdiv': 'Bulgaria',
            'Frankfurt': 'Germany',
            'Washington': 'USA',
            'Moscow': 'Russia'
        }
        self.expected = s.reversed_dict(self.data)

    def test_reversed_dict_with_duplicate_keys(self):
        self.assertEqual(
            sorted(self.expected.keys()),
            sorted(['Bulgaria', 'USA', 'Germany', 'Great Britain', 'Russia']))
        helper = list(map(lambda item: item in list(
            self.expected.values()), self.data.keys()))
        self.assertTrue(helper, self.data.keys())


class TestFlattenDict(unittest.TestCase):
    def test_flatten_without_nesting(self):
        self.assertEqual({'a': 1, 'b': 2}, s.flatten_dict({'a': 1, 'b': 2}))

    def test_flatten_with_one_dict_nesting(self):
        self.assertEqual({'a': 1, 'b.c': 2}, s.flatten_dict(
            {'a': 1, 'b': {'c': 2}}))

    def test_flatten_with_two_dicts_nesting(self):
        self.assertEqual({'b.c.d': 2}, s.flatten_dict(
            {'b': {'c': {'d': 2}}}))

    def test_flatten_with_two_dicts_nesting_second_level(self):
        self.assertEqual({'b.c.d': 2, 'b.f': 3}, s.flatten_dict(
            {'b': {'c': {'d': 2}, 'f': 3}}))

    def test_flatten_with_two_dicts_nesting_third_level(self):
        self.assertEqual({'b.c.d': 2, 'b.c.f': 3}, s.flatten_dict(
            {'b': {'c': {'d': 2, 'f': 3}}}))

    def test_flatten_with_three_dicts_nesting(self):
        self.assertEqual({'b.c.d.f': 2}, s.flatten_dict(
            {'b': {'c': {'d': {'f': 2}}}}))


class TestUnflattenDict(unittest.TestCase):
    def test_unflatten_without_nesting(self):
        self.assertEqual({'a': 1, 'b': 2}, s.unflatten_dict({'a': 1, 'b': 2}))

    def test_unflatten_with_one_dict_nesting(self):
        self.assertEqual({'a': 1, 'b': {'c': 2}}, s.unflatten_dict(
            {'a': 1, 'b.c': 2}))

    def test_unflatten_with_two_dicts_nesting(self):
        self.assertEqual({'b': {'c': {'d': 2}}}, s.unflatten_dict(
            {'b.c.d': 2}))

    def test_unflatten_with_two_dicts_nesting_second_level(self):
        self.assertEqual({'b': {'c': {'d': 2}, 'f': 3}}, s.unflatten_dict(
            {'b.c.d': 2, 'b.f': 3}))

    def test_unflatten_with_two_dicts_nesting_third_level(self):
        self.assertEqual({'b': {'c': {'d': 2, 'f': 3}}}, s.unflatten_dict(
            {'b.c.d': 2, 'b.c.f': 3}))

    def test_unflatten_with_three_dicts_nesting(self):
        self.assertEqual({'b': {'c': {'d': {'f': 2}}}}, s.unflatten_dict(
            {'b.c.d.f': 2}))


class TestReps(unittest.TestCase):
    def test_without_reps(self):
        self.assertEqual((), s.reps((1, 2, 3)))

    def test_with_one_repetition(self):
        self.assertEqual((1, 1), s.reps((1, 2, 3, 1, 5)))

    def test_with_more_repetition(self):
        self.assertEqual((1, 2, 2, 1), s.reps((1, 2, 2, 3, 1, 7)))


if __name__ == '__main__':
    unittest.main()
