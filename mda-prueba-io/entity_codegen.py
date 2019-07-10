"""
An example how to generate angularjs code from textX model using jinja2
template engine (http://jinja.pocoo.org/docs/dev/)
"""
from os import mkdir
from os.path import exists, dirname, join
import jinja2
from entity_test import get_entity_mm


def main(debug=False):

    this_folder = dirname(__file__)

    entity_mm = get_entity_mm(debug)

    # Build Certificate model from person.ent file
    person_model = entity_mm.model_from_file(join(this_folder, 'person.ent'))

    def is_entity(n):
        """
        Test to prove if some type is an certificate
        """
        if n.type in person_model.certificates:
            return True
        else:
            return False

    # Create output folder
    srcgen_folder = join(this_folder, 'srcgen')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    # Register filter for mapping Entity type names to Java type names.

    jinja_env.tests['certificate'] = is_entity
    jinja_env.tests['actividad'] = is_entity
    ##jinja_env.filters['javatype'] = javatype

  
    # Load template
    template = jinja_env.get_template('certificate.template')

    for certificate in person_model.certificates:
        # For each certificate generate html file
        with open(join(srcgen_folder,
                       "certificate%s.html" % certificate.name.capitalize()), 'w') as f:
            f.write(template.render(certificates=certificate))


if __name__ == "__main__":
    main()
