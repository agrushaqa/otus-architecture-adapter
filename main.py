import os.path

from data.class_info import ClassInfo


class GeneratorAdapter:
    def set_filename(self, file):
        self.target_file = file

    def set_clazz(self, clazz):
        self.clazz = clazz

    def execute(self):
        clazz = self.clazz
        content = ""
        content += self._gen_import(clazz)
        content += "\n"
        content += self._gen_class_caption(clazz)
        content += self._get_init_caption("obj", "ioc")
        content += self._gen_init_attr("obj", "ioc")
        content += self.gen_method(clazz)
        with open(os.path.join(ClassInfo.get_dir(clazz), self.target_file),
                  "w+") as (
                target_file_handler):
            target_file_handler.write(content)

    def _gen_class_caption(self, clazz):
        return f"class AutoGeneratedMovableAdapter({clazz.__name__}):\n"

    def _gen_import(self, clazz):
        return f"from {clazz.__module__} import {clazz.__name__}\n\n"

    def _gen_init_attr(self, *argv):
        result = ""
        for i_arg in argv:
            result += f"        self.{i_arg} = {i_arg}\n"
        return result

    def _get_init_caption(self, *argv):
        data = "    def __init__(self, "
        data += f"{ClassInfo._get_args_as_str(*argv)}):\n"
        return data

    def gen_method(self, clazz, default_list_param="self.obj"):
        context = ""
        for i_method in ClassInfo.get_list_methods(clazz):
            context += "\n"
            context += f"    def {i_method}"
            list_args = ClassInfo.get_method_properties(clazz, i_method)
            context += ClassInfo._get_args_as_str(
                list_args
            )
            context += ":\n"
            context += f"        self.ioc.resolve({clazz.__name__}"
            context += f".{i_method}, "
            context += f"{default_list_param}"
            list_args = list(list_args.parameters)
            list_args.remove("self")
            if not ClassInfo._get_args_as_str(list_args):
                context += ClassInfo._get_args_as_str(list_args)
            context += "\n                         ).execute()\n"
        return context
