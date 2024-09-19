# STRENDA DB

## Administration

## Data

### Publication

- title
  - Type: string
  - Description: title of the publication
- doi
  - Type: string
  - Description: identifier of the publication
- pmid
  - Type: string
  - Description: identifier of the publication as indexed in PubMed
- author
  - Type: Author
  - Multiple: true
- experiment
  - Type: Experiment
  - Multiple: true

### Author

- name
  - Type: string
  - Description: name of the author. Nomenclature: Family name initials first name
- affiliation
  - Type: string
  - Description: name of organizaton, department, city, country
- email
  - Type: string
  - Description: email address
- orcid
  - Type: string
  - Description: ORCID idenfier

## ProteinData

### Experiment

- name
  - Type: string
  - Description: name of the experiment, just for internal purposes
- assay_type
  - Type: string
  - Description: name of the assay
- direction_of_assay
  - Type: string
  - Description:
- compound_monitored
  - Type: string
  - Description:
- continuously_monitored
  - Type: string
  - Description: selection of the stopping procedure
- directly_monitored
  - Type: string
- protein_assay
  - Type: ProteinDescription

### ProteinDescription

- uniprotkb_id
  - Type: string
  - Description: identifier obtained from UniProtKB
- name
  - Type: string
  - Description: name of the protein as of UniProtKB
- sequence
  - Type: string
- modifications
  - Type: Modifications
- source
  - Type: ProteinSource
- reaction
  - Type: ProteinReaction
- characteristics
  - Type: Dataset
  - Multiple: true

### ProteinSource

- expression_system
  - Type: string
  - Description: Description of expression system if heterologously expressed
- organism
  - Type: string
  - Description: as in UniProtKB provided, name of organism
- taxon_id
  - Type: string
  - Description: ID as obtained from NCBI Taxonomy
- strain
  - Type: string
  - Description: name or identifier of the strain
- cell_type
  - Type: string
  - Description: determination of the cell in which the protein is expressed
- tissue
  - Type: string
  - Description: determination of the tissue, ideally BTO is used
- localization
  - Type: string
  - Description: determination of the localization (membran, cytosol, etc.)

### Modifications

- sequence_modification
  - Type: string
  - Description: modified amino acid sequence
- type_of_modification
  - Type: string
  - Description: Description of the Types of modifications
- determination_ptm
  - Type: string
  - Description: Phosphorylation, Glycosylation, Acetylation, Hydroxylation, Methylation, Other

### ProteinReaction

- ec_number
  - Type: string
  - Description: EC number obtained from ExplorEnz
- reaction_as_in_explorenz
  - Type: string
  - Description: reaction as described in ExplorEnz
- comment
  - Type: string
  - Description: comment on the protein reaction if not properly described in ExplorEnz

### Dataset

- name
  - Type: string
  - Description: name of the dataset
- assay_conditions
  - Type: AssayConditions
  - Multiple: true
- result_set
  - Type: ResultsSet
  - Multiple: true

### AssayConditions

- small_assay_components
  - Type: string[]
  - Description: Description of the compound used in the assay
- macro_molecular_components
  - Type: string[]
  - Description: Description of the macromolecular components
- protein_concentration
  - Type: float
  - Description: value with unit
- protein_concentration_unit
  - Type: string
  - Description: unit of the protein concentration
- description_of_concentration_measurement
  - Type: string
  - Description: free text field
- ph
  - Type: string
  - Description: value and unit
- pd
  - Type: string
  - Description: value and unit
- temperature
  - Type: string
  - Description: value and unit, K and Celsius

### SmallAssayComponents

- role
  - Type: string
  - Description: role in the assay, i.e. substrate, product, etc.
- initial_concentration_fixed
  - Type: string
  - Description: unit, value
- initial_concentration_varied
  - Type: string
  - Description: concentration range, value, unit
- compound_name
  - Type: string
  - Description: name as obtained from PubChem
- inchi
  - Type: string
  - Description: InChi string
- iupac
  - Type: string
  - Description: IUPAC name
- chebi_id
  - Type: string
  - Description: identifier
- pubchem_id
  - Type: string
  - Description: identifier

### MacromolecularComponents

- role
  - Type: string
  - Description: role in the assay, i.e. substrate, product, etc.
- initial_concentration_fixed
  - Type: string
  - Description: unit, value
- initial_concentration_varied
  - Type: string
  - Description: concentration range, value, unit
- classification
  - Type: string
  - Description: protein, carbohydrate, DNA, RNA, etc.
- compound_name
  - Type: string
  - Description: name as obtained from PubChem
- inchi
  - Type: string
  - Description: InChi string
- iupac
  - Type: string
  - Description: IUPAC name
- database used
  - Type: string
  - Description: name of the database
- identifier
  - Type: string
  - Description: identifier

### RoleOfComponent

- substrate
  - Type: string
  - Description: substrate of chemical reaction
- product
  - Type: string
  - Description: production of chemical reaction
- inhibitor
  - Type: string
  - Description: component that inhibits the chemical reaction
- activator
  - Type: string
  - Description: component that activates/enhances the chemical reaction

### ResultsSet

- initial_kinetics
  - Type: InitialKinetics
  - Description: Km, kcat, V, kcat/Km, V/Km
- activation
  - Type: Activation
- inhibition
  - Type: Inhibition

### InitialKinetics

- Km
  - Type: Parameter
  - descriptor: value, SE, unit
- kcat
  - Type: Parameter
  - descriptor: value, SE, unit
- V
  - Type: Parameter
  - descriptor: value, SE, unit
- kcat/Km
  - Type: Parameter
  - descriptor: value, SE, unit
- V/Km
  - Type: Parameter
  - descriptor: value, SE, unit

### Parameter

- value
  - Type: float
  - Description: value of the parameter
- standard_error
  - Type: float
  - Description: standard error of the parameter
- unit
  - Type: string
  - Description: unit of the parameter

### Activation

- affinity_constant
  - Type: string
  - descriptor: value, SE, unit, true or apparent
- velocity_no_activator
  - Type: string
  - Description: velocity without activator
- velocity_max_concentration
  - Type: string
  - Description: velocity at maximum concentration of activator
- saturation
  - Type: string
  - Description: statement whether the concentration was saturating or not
- influence_km_no_activator
  - Type: string
  - Description: Value, SE, Unit, true/apparent
- influence_max_concentration
  - Type: string
  - Description: Value, SE, Unit, true/apparent

### Inhibition

- reversibility
  - Type: string
  - Description: competitive, uncompetitive, mixed, kic, SE, Unit, Math function
- reversibility_no
  - Type: string
  - Description: ki, SE, Unit, Comment
