import inspect
import os.path


class ClassInfo:

    @staticmethod
    def get_dir(clazz):
        '''
        :param clazz: класс
        :return: папка в которой лежит файл с классом
        '''
        return os.path.dirname(
            inspect.getmodule(clazz).__file__)

    @staticmethod
    def _get_args_as_str(*argv):
        '''

        :param argv: Пример: "obj", "ioc"
        :return: "obj, ioc"
        '''
        list_arg = ""
        for i_arg in argv:
            if len(list_arg) > 0:
                list_arg += ", "
            list_arg += str(i_arg)
        return list_arg

    @staticmethod
    def get_method_properties(clazz, method_name):
        '''

        :param clazz:
        :param method_name:
        :return: список методов класса включая служебные
        '''
        return inspect.signature(clazz.__dict__[method_name])

    @staticmethod
    def get_list_methods(clazz):
        '''

        :param clazz:
        :return: список пользовательских методов класса
        '''
        return [func for func in dir(clazz)
                if callable(getattr(clazz, func))
                and not func.startswith("__")]
