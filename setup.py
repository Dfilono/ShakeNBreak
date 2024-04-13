'''Setup Package'''

from setuptools import setup

requirements = [
    'numpy',
    'TurtleMol',
]

setup_requirements = []
test_requirements = requirements.append(['pytest'])

setup(
    name = 'ShakeNBreak',
    python_requires = '>=3.7',
    packages = ['ShakeNBreak'],
    install_requires=requirements,
    include_package_data=True,
    setup_requires=setup_requirements,
    maintainer = 'Dominick Filonowich',
    maintainer_email = 'dof13@pitt.edu',
    test_suite="tests",
    tests_require=test_requirements,
    version=0.1,
    zip_safe=False,
)
