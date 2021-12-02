import unittest
import unittest.mock

from mcstasscript.helper.mcstas_objects import ParameterVariable


class Test_ParameterVariable(unittest.TestCase):
    """
    Tests the ParameterVariable class that holds an input parameter
    for the instrument.

    """

    def test_ParameterVariable_init_basic(self):
        """
        Smallest possible initialization
        """

        par = ParameterVariable("test")
        self.assertEqual(par.name, "test")

    def test_ParameterVariable_init_basic_type(self):
        """
        Initialization with a type
        """

        par = ParameterVariable("double", "test")

        self.assertEqual(par.name, "test")
        self.assertEqual(par.type, "double")

    def test_ParameterVariable_init_basic_type_value(self):
        """
        Initialization with type and value
        """

        par = ParameterVariable("double", "test", value=518)

        self.assertEqual(par.name, "test")
        self.assertEqual(par.type, "double")
        self.assertEqual(par.value, 518)

    def test_ParameterVariable_init_basic_type_value_comment(self):
        """
        Initialization with type, value and comment
        """

        par = ParameterVariable("double", "test", value=518,
                                comment="test comment /")

        self.assertEqual(par.name, "test")
        self.assertEqual(par.type, "double")
        self.assertEqual(par.value, 518)
        self.assertEqual(par.comment, "test comment /")

    def test_ParameterVariable_init_basic_value_comment(self):
        """
        Initialization with value and comment
        """

        par = ParameterVariable("test", value=518,
                                comment="test comment /")

        self.assertEqual(par.name, "test")
        self.assertEqual(par.type, "")
        self.assertEqual(par.value, 518)
        self.assertEqual(par.comment, "test comment /")

    def test_ParameterVariable_init_options_initialize(self):
        """
        Initialization with value and comment
        """

        par = ParameterVariable("test", value=2,
                                options=[1, 2, "horse"])

        self.assertEqual(par.name, "test")
        self.assertEqual(par.type, "")
        self.assertEqual(par.value, 2)
        self.assertEqual(par.options, [1, 2, "horse"])

    @unittest.mock.patch('__main__.__builtins__.open',
                         new_callable=unittest.mock.mock_open)
    def test_ParameterVariable_write_basic(self, mock_f):
        """
        Testing that write to file is correct. Here a line is in an
        instrument parameter section. The write file operation is
        mocked and check using a patch. Here a simple parameter is
        used.
        """

        par = ParameterVariable("double", "test")
        with mock_f('test.txt', 'w') as m_fo:
            par.write_parameter(m_fo, "")

        expected_writes = [unittest.mock.call("double test"),
                           unittest.mock.call(""),
                           unittest.mock.call(""),
                           unittest.mock.call("\n")]

        mock_f.assert_called_with('test.txt', 'w')
        handle = mock_f()
        handle.write.assert_has_calls(expected_writes, any_order=False)

    @unittest.mock.patch('__main__.__builtins__.open',
                         new_callable=unittest.mock.mock_open)
    def test_ParameterVariable_write_complex_float(self, mock_f):
        """
        Testing that write to file is correct. Here a line is in an
        instrument parameter section. The write file operation is
        mocked and check using a patch. Here a parameter with a value
        is used. (float value)
        """

        par = ParameterVariable("double", "test", value=5.4,
                                comment="test comment")

        with mock_f('test.txt', 'w') as m_fo:
            par.write_parameter(m_fo, ")")

        expected_writes = [unittest.mock.call("double test"),
                           unittest.mock.call(" = 5.4"),
                           unittest.mock.call(")"),
                           unittest.mock.call("// test comment"),
                           unittest.mock.call("\n")]

        mock_f.assert_called_with('test.txt', 'w')
        handle = mock_f()
        handle.write.assert_has_calls(expected_writes, any_order=False)

    @unittest.mock.patch('__main__.__builtins__.open',
                         new_callable=unittest.mock.mock_open)
    def test_ParameterVariable_write_complex_int(self, mock_f):
        """
        Testing that write to file is correct. Here a line is in an
        instrument parameter section. The write file operation is
        mocked and check using a patch. Here a parameter with a value
        is used. (integer value)
        """

        par = ParameterVariable("double", "test", value=5,
                                comment="test comment")

        with mock_f('test.txt', 'w') as m_fo:
            par.write_parameter(m_fo, ")")

        expected_writes = [unittest.mock.call("double test"),
                           unittest.mock.call(" = 5"),
                           unittest.mock.call(")"),
                           unittest.mock.call("// test comment"),
                           unittest.mock.call("\n")]

        mock_f.assert_called_with('test.txt', 'w')
        handle = mock_f()
        handle.write.assert_has_calls(expected_writes, any_order=False)

    @unittest.mock.patch('__main__.__builtins__.open',
                         new_callable=unittest.mock.mock_open)
    def test_ParameterVariable_write_complex_string(self, mock_f):
        """
        Testing that write to file is correct. Here a line is in an
        instrument parameter section. The write file operation is
        mocked and check using a patch. Here a parameter with a value
        is used. (string value)
        """

        par = ParameterVariable("double", "test", value="\"Al\"",
                                comment="test comment")

        with mock_f('test.txt', 'w') as m_fo:
            par.write_parameter(m_fo, ",")

        expected_writes = [unittest.mock.call("double test"),
                           unittest.mock.call(" = \"Al\""),
                           unittest.mock.call(","),
                           unittest.mock.call("// test comment"),
                           unittest.mock.call("\n")]

        mock_f.assert_called_with('test.txt', 'w')
        handle = mock_f()
        handle.write.assert_has_calls(expected_writes, any_order=False)


if __name__ == '__main__':
    unittest.main()
