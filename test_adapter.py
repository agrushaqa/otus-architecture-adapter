import os

from data.class_info import ClassInfo
from data.imovable import TankOperationsIMovable
from main import GeneratorAdapter


class TestAdapter:
    def test_generate_class_by_interface(self):
        generator = GeneratorAdapter()
        generator.set_filename("autogen_target.py")
        generator.set_clazz(TankOperationsIMovable)
        generator.execute()
        expected_file_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "test_data", "autogen_target.py"
        )
        with open(expected_file_path) as expected_file_handler:
            expected_content = expected_file_handler.read()

        with open(os.path.join(ClassInfo.get_dir(TankOperationsIMovable),
                               "autogen_target.py")) as target_file_handler:
            actual_content = target_file_handler.read()
        assert actual_content == expected_content
