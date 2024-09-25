---
hide:
    - navigation
---

# STRENDA DB

This page provides comprehensive information about the structure and components of the data model, including detailed descriptions of the types and their properties, information on enumerations, and an overview of the ontologies used and their associated prefixes. Below, you will find a graph that visually represents the overall structure of the data model.

??? quote "Graph"
    ``` mermaid
    flowchart TB
        publication(Publication)
        author(Author)
        experiment(Experiment)
        proteindescription(ProteinDescription)
        proteinsource(ProteinSource)
        sequencemodifications(SequenceModifications)
        posttranslationalmodifications(PosttranslationalModifications)
        proteinreaction(ProteinReaction)
        dataset(Dataset)
        assayconditions(AssayConditions)
        smallassaycomponents(SmallAssayComponents)
        macromolecularcomponents(MacromolecularComponents)
        roleofcomponent(RoleOfComponent)
        compoundclassification(CompoundClassification)
        resultsset(ResultsSet)
        initialkineticsparameters(InitialKineticsParameters)
        activation(Activation)
        inhibition(Inhibition)
        publication(Publication) --> author(Author)
        publication(Publication) --> experiment(Experiment)
        experiment(Experiment) --> proteindescription(ProteinDescription)
        proteindescription(ProteinDescription) --> sequencemodifications(SequenceModifications)
        proteindescription(ProteinDescription) --> posttranslationalmodifications(PosttranslationalModifications)
        proteindescription(ProteinDescription) --> proteinsource(ProteinSource)
        proteindescription(ProteinDescription) --> proteinreaction(ProteinReaction)
        proteindescription(ProteinDescription) --> dataset(Dataset)
        dataset(Dataset) --> assayconditions(AssayConditions)
        dataset(Dataset) --> resultsset(ResultsSet)
        assayconditions(AssayConditions) --> smallassaycomponents(SmallAssayComponents)
        assayconditions(AssayConditions) --> macromolecularcomponents(MacromolecularComponents)
        macromolecularcomponents(MacromolecularComponents) --> roleofcomponent(RoleOfComponent)
        resultsset(ResultsSet) --> initialkineticsparameters(InitialKineticsParameters)
        resultsset(ResultsSet) --> activation(Activation)
        resultsset(ResultsSet) --> inhibition(Inhibition)

        click publication "#publication" "Go to Publication"
        click author "#author" "Go to Author"
        click experiment "#experiment" "Go to Experiment"
        click proteindescription "#proteindescription" "Go to ProteinDescription"
        click proteinsource "#proteinsource" "Go to ProteinSource"
        click sequencemodifications "#sequencemodifications" "Go to SequenceModifications"
        click posttranslationalmodifications "#posttranslationalmodifications" "Go to PosttranslationalModifications"
        click proteinreaction "#proteinreaction" "Go to ProteinReaction"
        click dataset "#dataset" "Go to Dataset"
        click assayconditions "#assayconditions" "Go to AssayConditions"
        click smallassaycomponents "#smallassaycomponents" "Go to SmallAssayComponents"
        click macromolecularcomponents "#macromolecularcomponents" "Go to MacromolecularComponents"
        click roleofcomponent "#roleofcomponent" "Go to RoleOfComponent"
        click compoundclassification "#compoundclassification" "Go to CompoundClassification"
        click resultsset "#resultsset" "Go to ResultsSet"
        click initialkineticsparameters "#initialkineticsparameters" "Go to InitialKineticsParameters"
        click activation "#activation" "Go to Activation"
        click inhibition "#inhibition" "Go to Inhibition"
    ```


## Types


### Publication
This is the publication that includes the experimental results of an enzyme kinetics characterization.

__title__* `string`

- Title of the publication


__doi__ `string`

- identifier of the publication


__pmid__ `string`

- identifier of the publication as indexed in PubMed


__author__ [`list[Author]`](#author)


__experiment__ [`list[Experiment]`](#experiment)


------

### Author


__name__* `string`

- name of the author. Nomenclature: Family name initials first name


__affiliation__ `string`

- name of organizaton, department, city, country


__email__ `string`

- email address


__orcid__ `string`

- ORCID idenfier


------

### Experiment


__name_of_experiment__ `string`

- name of the experiment, just for internal purposes


__type_of_assay__ `string`

- name of the assay


__direction_of_the_assay__ `string`


__definition_of_the_compound_monitored__ `string`


__continuously_monitored__ `string`

- selection of the stopping procedure


__directly_monitored__ `string`


__protein_assay__ [`ProteinDescription`](#proteindescription)


------

### ProteinDescription


__uniprotkb_ac__ `string`

- identifier obtained from UniProtKB


__protein_name__ `string`

- name of the protein as of UniProtKB


__protein_sequence__ [`SequenceModifications`](#sequencemodifications)

- amino acid sequence as from UniProtKB


__posttranslational_modifications__ [`PosttranslationalModifications`](#posttranslationalmodifications)


__protein_source__ [`ProteinSource`](#proteinsource)


__reaction__ [`ProteinReaction`](#proteinreaction)


__protein_characterization__ [`list[Dataset]`](#dataset)


------

### ProteinSource


__expression_system__ `string`

- Description of expression system if heterologously expressed


__organism__ `string`

- as in UniProtKB provided, name of organism


__taxon_id__ `string`

- ID as obtained from NCBI Taxonomy


__strain__ `string`

- name or identifier of the strain


__cell_type__ `string`

- determination of the cell in which the protein is expressed


__tissue__ `string`

- determination of the tissue, ideally BTO is used


__localization__ `string`

- determination of the localization (membran, cytosol, etc.)


------

### SequenceModifications


__sequence_modification__ `string`

- modified amino acid sequence


__specification_of_the_type_of_modification__ `string`

- Description of the types of modifications


------

### PosttranslationalModifications


__determination_of_ptm__ `string`

- Phosphorylation, Glycosylation, Acetylation, Hydroxylation, Methylation, Other


------

### ProteinReaction


__ec_number__ `string`

- EC number obtained from ExplorEnz


__reaction_as_in_explorenz__ `string`

- reaction as described in ExplorEnz


__comment__ `string`

- comment on the protein reaction if not properly described in ExplorEnz


------

### Dataset


__name__ `string`

- name of the dataset


__assay_conditions__ [`list[AssayConditions]`](#assayconditions)


__results_set__ [`list[ResultsSet]`](#resultsset)


__doi__ `string`

- DOI of the dataset


------

### AssayConditions


__small_assay_components__ [`SmallAssayComponents`](#smallassaycomponents)

- Description of the compound used in the assay


__macromolecular_components__ [`MacromolecularComponents`](#macromolecularcomponents)

- Description of the macromolecular components


__concentration_of_the_assayed_protein__ `string`

- value with unit


__description_of_concentration_measurement__ `string`

- free text field


__ph__ `string`

- value and unit


__pd__ `string`

- value and unit


__temperature__ `string`

- value and unit, K and Celsius


------

### SmallAssayComponents


__role__ `string`

- role in the assay, i.e. substrate, product, etc.


__initial_concentration_fixed__ `string`

- unit, value


__initial_concentration_varied__ `string`

- concentration range, value, unit


__compound_name__ `string`

- name as obtained from PubChem


__inchi__ `string`

- InChi string


__iupac__ `string`

- IUPAC name


__chebi_id__ `string`

- identifier


__pubchem_cid__ `string`

- identifier


------

### MacromolecularComponents


__role__ [`RoleOfComponent`](#roleofcomponent)

- role in the assay, i.e. substrate, product, etc.


__initial_concentration_fixed__ `string`

- unit, value


__initial_concentration_varied__ `string`

- concentration range, value, unit


__classification__ `string`

- protein, carbohydrate, DNA, RNA, etc.


__compound_name__ `string`

- name as obtained from PubChem


__inchi__ `string`

- InChi string


__iupac__ `string`

- IUPAC name


__database_used__ `string`

- name of the database


__identifier__ `string`

- identifier


------

### RoleOfComponent


__substrate__ `string`

- substrate of chemical reaction


__product__ `string`

- production of chemical reaction


__inhibitor__ `string`

- component that inhibits the chemical reaction


__activator__ `string`

- component that activates/enhances the chemical reaction


------

### CompoundClassification


__protein__ `string`


__carbohydrate__ `string`


__dna__ `string`


__rna__ `string`


__lipid__ `string`


__other__ `string`


------

### ResultsSet


__name__ `string`

- Name of the results set


__initial_kinetic_parameters__ [`InitialKineticsParameters`](#initialkineticsparameters)

- Km, kcat, V, kcat/Km, V/Km


__activation__ [`Activation`](#activation)


__inhibition__ [`Inhibition`](#inhibition)


------

### InitialKineticsParameters


__km__ `string`

- `Descriptor`: value, SE, unit

__kcat__ `string`

- `Descriptor`: value, SE, unit

__v__ `string`

- `Descriptor`: value, SE, unit

__kcat_over_km__ `string`

- `Descriptor`: value, SE, unit

__v_over_km__ `string`

- `Descriptor`: value, SE, unit

------

### Activation


__affinity_constant__ `string`

- `Descriptor`: value, SE, unit, true or apparent

__velocity_no_activator__ `string`

- velocity without activator


__velocity_at_max_concentration__ `string`

- velocity at maximum concentration of activator


__saturation__ `string`

- statement whether the concentration was saturating or not


__incluence_no_activator__ `string`

- Influence on MM kinetics. Schema: Value, SE, Unit, true/apparent


__influence_at_maxconcentration__ `string`

- Influence on MM kinetics. Schema: Value, SE, Unit, true/apparent


------

### Inhibition


__reversibility_yes__ `string`

- inhbition type - competitive, uncompetitive, mixed, kic, SE, Unit, Math function


__reversibility_no__ `string`

- ki, SE, Unit, Comment