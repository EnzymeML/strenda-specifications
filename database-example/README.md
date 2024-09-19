# Setting up a PostgreSQL database and STRENDA-DB Light

The following example demonstrates how to set up a PostgreSQL database using Docker and sdRDM-DB. Here we will make use of the `create_tables` functionality to build the necessary tables for the database.

## Docker installation

To install Docker, follow the instructions provided in the [official documentation](https://docs.docker.com/get-docker/).

## Database setup

This example includes a `docker-compose` recipe to spawn a new instance of a PostgreSQL database. For this, run the following command:

```bash
mkdir data
sudo docker-compose up -d
```

_(The `sudo` command may only be necessary for linux dists)_

## Create tables

Once the database is up and running, you can create the tables by running the following command:

```bash
python3 create_tables.py
```

_Output_

```bash
🎉 Connected

🚀 Creating tables for data model ../specifications/STRENDADB_light_20240904_fix.md
│
├── Table __model_meta__ not existing. Adding to DB!
├── Added table model 'DATA_MODEL' to __model_meta__ table
├── Added table model 'Publication' to __model_meta__ table
├── Added table model 'Author' to __model_meta__ table
├── Added table model 'Experiment' to __model_meta__ table
├── Added table model 'ProteinDescription' to __model_meta__ table
├── Added table model 'ProteinSource' to __model_meta__ table
├── Added table model 'SequenceModifications' to __model_meta__ table
├── Added table model 'PosttranslationalModifications' to __model_meta__ table
├── Added table model 'ProteinReaction' to __model_meta__ table
├── Added table model 'Dataset' to __model_meta__ table
├── Added table model 'AssayConditions' to __model_meta__ table
├── Added table model 'SmallAssayComponents' to __model_meta__ table
├── Added table model 'MacromolecularComponents' to __model_meta__ table
├── Added table model 'RoleOfComponent' to __model_meta__ table
├── Added table model 'CompoundClassification' to __model_meta__ table
├── Added table model 'ResultsSet' to __model_meta__ table
├── Added table model 'InitialKineticsParameters' to __model_meta__ table
├── Added table model 'Activation' to __model_meta__ table
├── Added table model 'Inhibition' to __model_meta__ table
├── Created table 'Publication'
├── Created table 'Author'
├── Created table 'Experiment'
├── Created table 'ProteinDescription'
├── Created table 'ProteinSource'
├── Created table 'SequenceModifications'
├── Created table 'PosttranslationalModifications'
├── Created table 'ProteinReaction'
├── Created table 'Dataset'
├── Created table 'AssayConditions'
├── Created table 'SmallAssayComponents'
├── Created table 'MacromolecularComponents'
├── Created table 'RoleOfComponent'
├── Created table 'CompoundClassification'
├── Created table 'ResultsSet'
├── Created table 'InitialKineticsParameters'
├── Created table 'Activation'
├── Created table 'Inhibition'
├── Added primary key 'id' to table Publication
├── Added primary key 'id' to table Author
├── Added primary key 'id' to table Experiment
├── Added primary key 'id' to table ProteinDescription
├── Added primary key 'id' to table ProteinSource
├── Added primary key 'id' to table SequenceModifications
├── Added primary key 'id' to table PosttranslationalModifications
├── Added primary key 'id' to table ProteinReaction
├── Added primary key 'id' to table Dataset
├── Added primary key 'id' to table AssayConditions
├── Added primary key 'id' to table SmallAssayComponents
├── Added primary key 'id' to table MacromolecularComponents
├── Added primary key 'id' to table RoleOfComponent
├── Added primary key 'id' to table CompoundClassification
├── Added primary key 'id' to table ResultsSet
├── Added primary key 'id' to table InitialKineticsParameters
├── Added primary key 'id' to table Activation
├── Added primary key 'id' to table Inhibition
├── Added join table 'Publication_author_Author'
├── Added join table 'Publication_experiment_Experiment'
├── Added foreign key 'protein_assay__fk' to table 'Experiment'
├── Added foreign key 'protein_sequence__fk' to table 'ProteinDescription'
├── Added foreign key 'posttranslational_modifications__fk' to table 'ProteinDescription'
├── Added foreign key 'protein_source__fk' to table 'ProteinDescription'
├── Added foreign key 'reaction__fk' to table 'ProteinDescription'
├── Added join table 'ProteinDescription_protein_characterization_Dataset'
├── Added join table 'Dataset_assay_conditions_AssayConditions'
├── Added join table 'Dataset_results_set_ResultsSet'
├── Added foreign key 'small_assay_components__fk' to table 'AssayConditions'
├── Added foreign key 'macromolecular_components__fk' to table 'AssayConditions'
├── Added foreign key 'role__fk' to table 'MacromolecularComponents'
├── Added foreign key 'initial_kinetic_parameters__fk' to table 'ResultsSet'
├── Added foreign key 'activation__fk' to table 'ResultsSet'
├── Added foreign key 'inhibition__fk' to table 'ResultsSet'
│
╰── 🎉 Created all tables for data model ../specifications/STRENDADB_light_20240904_fix.md
```

## Working with the database

In the Jupyter notebook `UseDatabase.ipynb`, you can find an example of how to interact with the database using the `sdrdm-db` library.
