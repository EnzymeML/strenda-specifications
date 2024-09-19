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
        modifications(Modifications)
        proteinreaction(ProteinReaction)
        dataset(Dataset)
        assayconditions(AssayConditions)
        smallassaycomponents(SmallAssayComponents)
        macromolecularcomponents(MacromolecularComponents)
        roleofcomponent(RoleOfComponent)
        resultsset(ResultsSet)
        initialkinetics(InitialKinetics)
        parameter(Parameter)
        activation(Activation)
        inhibition(Inhibition)
        publication(Publication) --> author(Author)
        publication(Publication) --> experiment(Experiment)
        experiment(Experiment) --> proteindescription(ProteinDescription)
        proteindescription(ProteinDescription) --> modifications(Modifications)
        proteindescription(ProteinDescription) --> proteinsource(ProteinSource)
        proteindescription(ProteinDescription) --> proteinreaction(ProteinReaction)
        proteindescription(ProteinDescription) --> dataset(Dataset)
        dataset(Dataset) --> assayconditions(AssayConditions)
        dataset(Dataset) --> resultsset(ResultsSet)
        resultsset(ResultsSet) --> initialkinetics(InitialKinetics)
        resultsset(ResultsSet) --> activation(Activation)
        resultsset(ResultsSet) --> inhibition(Inhibition)
        initialkinetics(InitialKinetics) --> parameter(Parameter)
        initialkinetics(InitialKinetics) --> parameter(Parameter)
        initialkinetics(InitialKinetics) --> parameter(Parameter)
        initialkinetics(InitialKinetics) --> parameter(Parameter)
        initialkinetics(InitialKinetics) --> parameter(Parameter)

        click publication "#publication" "Go to Publication"
        click author "#author" "Go to Author"
        click experiment "#experiment" "Go to Experiment"
        click proteindescription "#proteindescription" "Go to ProteinDescription"
        click proteinsource "#proteinsource" "Go to ProteinSource"
        click modifications "#modifications" "Go to Modifications"
        click proteinreaction "#proteinreaction" "Go to ProteinReaction"
        click dataset "#dataset" "Go to Dataset"
        click assayconditions "#assayconditions" "Go to AssayConditions"
        click smallassaycomponents "#smallassaycomponents" "Go to SmallAssayComponents"
        click macromolecularcomponents "#macromolecularcomponents" "Go to MacromolecularComponents"
        click roleofcomponent "#roleofcomponent" "Go to RoleOfComponent"
        click resultsset "#resultsset" "Go to ResultsSet"
        click initialkinetics "#initialkinetics" "Go to InitialKinetics"
        click parameter "#parameter" "Go to Parameter"
        click activation "#activation" "Go to Activation"
        click inhibition "#inhibition" "Go to Inhibition"
    ```


## Types


### Publication


__title__ `string`

- title of the publication


__doi__ `string`

- identifier of the publication


__pmid__ `string`

- identifier of the publication as indexed in PubMed


__author__ [`list[Author]`](#author)


__experiment__ [`list[Experiment]`](#experiment)


------

### Author


__name__ `string`

- name of the author. Nomenclature: Family name initials first name


__affiliation__ `string`

- name of organizaton, department, city, country


__email__ `string`

- email address


__orcid__ `string`

- ORCID idenfier


------

### Experiment


__name__ `string`

- name of the experiment, just for internal purposes


__assay_type__ `string`

- name of the assay


__direction_of_assay__ `string`


__compound_monitored__ `string`


__continuously_monitored__ `string`

- selection of the stopping procedure


__directly_monitored__ `string`


__protein_assay__ [`ProteinDescription`](#proteindescription)


------

### ProteinDescription


__uniprotkb_id__ `string`

- identifier obtained from UniProtKB


__name__ `string`

- name of the protein as of UniProtKB


__sequence__ `string`


__modifications__ [`Modifications`](#modifications)


__source__ [`ProteinSource`](#proteinsource)


__reaction__ [`ProteinReaction`](#proteinreaction)


__characteristics__ [`list[Dataset]`](#dataset)


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

### Modifications


__sequence_modification__ `string`

- modified amino acid sequence


__type_of_modification__ `string`

- Description of the Types of modifications


__determination_ptm__ `string`

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


__result_set__ [`list[ResultsSet]`](#resultsset)


------

### AssayConditions


__small_assay_components__ `list[string]`

- Description of the compound used in the assay


__macro_molecular_components__ `list[string]`

- Description of the macromolecular components


__protein_concentration__ `float`

- value with unit


__protein_concentration_unit__ `string`

- unit of the protein concentration


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


__pubchem_id__ `string`

- identifier


------

### MacromolecularComponents


__role__ `string`

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


__database used__ `string`

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

### ResultsSet


__initial_kinetics__ [`InitialKinetics`](#initialkinetics)

- Km, kcat, V, kcat/Km, V/Km


__activation__ [`Activation`](#activation)


__inhibition__ [`Inhibition`](#inhibition)


------

### InitialKinetics


__Km__ [`Parameter`](#parameter)

- `Descriptor`: value, SE, unit

__kcat__ [`Parameter`](#parameter)

- `Descriptor`: value, SE, unit

__V__ [`Parameter`](#parameter)

- `Descriptor`: value, SE, unit

__kcat/Km__ [`Parameter`](#parameter)

- `Descriptor`: value, SE, unit

__V/Km__ [`Parameter`](#parameter)

- `Descriptor`: value, SE, unit

------

### Parameter


__value__ `float`

- value of the parameter


__standard_error__ `float`

- standard error of the parameter


__unit__ `string`

- unit of the parameter


------

### Activation


__affinity_constant__ `string`

- `Descriptor`: value, SE, unit, true or apparent

__velocity_no_activator__ `string`

- velocity without activator


__velocity_max_concentration__ `string`

- velocity at maximum concentration of activator


__saturation__ `string`

- statement whether the concentration was saturating or not


__influence_km_no_activator__ `string`

- Value, SE, Unit, true/apparent


__influence_max_concentration__ `string`

- Value, SE, Unit, true/apparent


------

### Inhibition


__reversibility__ `string`

- competitive, uncompetitive, mixed, kic, SE, Unit, Math function


__reversibility_no__ `string`

- ki, SE, Unit, Comment