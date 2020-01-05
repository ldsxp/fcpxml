def _generate_fields(element):
    """
    生成字段(帮助我们开发)
    """
    l = [f"self.{element_child.tag} = None"
         for element_child in element]
    ll = [f"elif element_child.tag == '{element_child.tag}': self.{element_child.tag} = element_child.text"
          for element_child in element]
    print('-' * 70)
    print("\n".join(l))
    print("\n".join(ll))
    print('=' * 70)
