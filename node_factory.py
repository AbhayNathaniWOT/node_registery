class NodeFactory:
    registry = {}

    @classmethod
    def get_node(cls, class_name):

        node_class = cls.registry[class_name]
        node = node_class()
        return node

    @classmethod
    def register(cls, class_name):
        def inner_wrapper(wrapped_class):
            if class_name not in cls.registry:
                cls.registry[class_name] = wrapped_class.module()
            else:
                print("Class Exist")
            return wrapped_class
        return inner_wrapper

    @classmethod
    def get_registry(cls):
        return cls.registry
