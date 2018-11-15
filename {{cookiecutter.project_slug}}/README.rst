{{ cookiecutter.project_name }}
==============================

{{ cookiecutter.project_description }}

.. image:: https://img.shields.io/badge/built%20with-cookiecutter%20falcon-brightgreen.svg
     :target: https://github.com/next-miguelreguero/cookiecutter-falcon
     :alt: Built with Cookiecutter Falcon

{% if cookiecutter.open_source_license != "Not open source" %}
LICENSE: {{ cookiecutter.open_source_license }}
{% endif %}

Deployment
----------
Local
^^^^^

To deploy the app locally (for testing/development), you will need to:
#. Create a virtualenv (basic).
#. Install application package as develop.
   .. code-block:: bash
        python setup.py develop
#. Serve the application itself:
   .. code-block:: bash
        export FALCON_SETTINGS_MODULE={{cookiecutter.project_slug}}.settings.local
        gunicorn {{ cookiecutter.project_slug }}.main:app --bind:127.0.0.1:8000 --reload

   Or
   
   .. code-block:: bash
        python {{ cookiecutter.project_slug}}/main.py

{% if cookiecutter.use_docker == "y" %}

Docker
^^^^^^

To tun docker container application you just need to run:
{% endif %}
