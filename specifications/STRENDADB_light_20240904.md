# STRENDA DB

## Administration

## Data

### Publication

This is the publication that includes the experimental results of an enzyme kinetics characterization.

* **Title**
  * type: string
  * description: title of the publication
* DOI
  * type: string
  * description: identifier of the publication
* PMID
  * type: string
  * description: identifier of the publication as indexed in PubMed
* Author
  * type: Author
  * Multiple: true
* Experiment
  * type: Experiment
  * Multiple: true

### Author

* **Name**
  * type: string
  * description: name of the author. Nomenclature: Family name initials first name
* Affiliation
  * type: string
  * description: name of organizaton, department, city, country
* Email
  * type: string
  * description: email address
* ORCID
  * type: string
  * description: ORCID idenfier

### Experiment

* Name of Experiment
  * type: string
  * description: name of the experiment, just for internal purposes
* Type of Assay
  * type: string
  * description: name of the assay
* Direction of the Assay
  * type: string
  * description:
* Definition of the compound monitored
  * type: string
  * description:
* Continuously monitored
  * type: string
  * description: selection of the stopping procedure
  * type: string
  * description: other
  * type: string
* Directly monitored
  * type: string
* Protein Assay
  * type: ProteinDescription
  * Multiple: false

### ProteinDescription

* UniProtKB AC
  * type: string
  * description: identifier obtained from UniProtKB
* Protein name
  * type: string
  * description: name of the protein as of UniProtKB
* Protein Sequence
  * type: SequenceModifications
  * description: amino acid sequence as from UniProtKB
* Posttranslational modifications
  * type: PosttranslationalModifications
* Protein Source
  * type: ProteinSource
* Reaction
  * type: ProteinReaction
* Protein characterization
  * type: Dataset
  * Multiple: true

### ProteinSource

* Expression system
  * type: string
  * description: description of expression system if heterologously expressed
* Organism
  * type: string
  * description: as in UniProtKB provided, name of organism
* Taxon ID
  * type: string
  * description: ID as obtained from NCBI Taxonomy
* Strain
  * type: string
  * description: name or identifier of the strain
* Cell Type
  * type: string
  * description: determination of the cell in which the protein is expressed
* Tissue
  * type: string
  * description: determination of the tissue, ideally BTO is used
* Localization
  * type: string
  * description: determination of the localization (membran, cytosol, etc.)

### SequenceModifications

* Sequence modification
  * type: string
  * description: modified amino acid sequence
* Specification of the type of modification
  * type: string
  * description: description of the types of modifications

### PosttranslationalModifications

* Determination of PTM
  * type: string
  * description: Phosphorylation, Glycosylation, Acetylation, Hydroxylation, Methylation, Other

### ProteinReaction

* EC number
  * type: string
  * description: EC number obtained from ExplorEnz
* Reaction as in ExplorEnz
  * type: string
  * description: reaction as described in ExplorEnz
* Comment
  * type: string
  * description: comment on the protein reaction if not properly described in ExplorEnz

### Dataset

* Name
  * type: string
  * description: name of the dataset
* Assay conditions
  * type: AssayConditions
  * Multiple: true
* Results Set
  * type: ResultsSet
  * Multiple: true
* DOI
  * type: string
  * description: DOI of the dataset

### AssayConditions

* Small Assay Components
  * type: Small\_Assay\_Components
  * description: description of the compound used in the assay
* Macromolecular Components
  * type: Macromolecular\_Components
  * description: description of the macromolecular components
* Concentration of the assayed protein
  * type: string
  * description: value with unit
* Description of concentration measurement
  * type: string
  * description: free text field
* pH
  * type: string
  * description: value and unit
* pD
  * type: string
  * description: value and unit
* Temperature
  * type: string
  * description: value and unit, K and Celsius

### Small\_Assay\_Components

* Role
  * type: Role\_of\_Component
  * description: role in the assay, i.e. substrate, product, etc.
* Initial concentration - fixed
  * type: string
  * description: unit, value
* Initial concentration - varied
  * type: string
  * description: concentration range, value, unit
* Compound name
  * type: string
  * description: name as obtained from PubChem
* InChi
  * type: string
  * description: InChi string
* IUPAC
  * type: string
  * description: IUPAC name
* ChEBI ID
  * type: string
  * description: identifier
* PubChem CID
  * type: string
  * description: identifier

### Macromolecular\_Components

* Role
  * type: Role\_of\_Component
  * description: role in the assay, i.e. substrate, product, etc.
* Initial concentration - fixed
  * type: string
  * description: unit, value
* Initial concentration - varied
  * type: string
  * description: concentration range, value, unit
* Class
  * type: Class
  * description: protein, carbohydrate, DNA, RNA, etc.
* Compound name
  * type: string
  * description: name as obtained from PubChem
* InChi
  * type: string
  * description: InChi string
* IUPAC
  * type: string
  * description: IUPAC name
* Database used
  * type: string
  * description: name of the database
* Identifier
  * type: string
  * description: identifier

### Role\_of\_Component

* Substrate
  * type: string
  * description: substrate of chemical reaction
* Product
  * type: string
  * description: production of chemical reaction
* Inhibitor
  * type: string
  * description: component that inhibits the chemical reaction
* Activator
  * type: string
  * description: component that activates/enhances the chemical reaction

### Class

* Protein
  * type: string
* Carbohydrate
  * type: string
* DNA
  * type: string
* RNA
  * type: string
* Lipid
  * type: string
* Other
  * type: string

### ResultsSet

* Initial Kinetic Parameters
  * type: Initial\_Kinetics\_Parameters
  * description: Km, kcat, V, kcat/Km, V/Km
* Activation
  * type: Activation
* Inhibition
  * type: Inhibition
  *

### Initial\_Kinetics\_Parameters

* Km
  * type: string
  * descriptor: value, SE, unit
* kcat
  * type: string
  * descriptor: value, SE, unit
* V
  * type: string
  * descriptor: value, SE, unit
* kcat/Km
  * type: string
  * descriptor: value, SE, unit
* V/Km
  * type: string
  * descriptor: value, SE, unit

### Activation

* Affinity constant
  * type: string
  * descriptor: value, SE, unit, true or apparent
* Reaction velocity
* no activator
  * type: string
  * description: velocity without activator
* at max. concentration
  * type: string
  * description: velocity at maximum concentration of activator
* Saturation
  * type: string
  * description: statement whether the concentration was saturating or not
* Influence on substrate MM kinetics
  * Km no activator
    * type: string
    * description: Value, SE, Unit, true/apparent
  * at max. concentration
    * type: string
    * description: Value, SE, Unit, true/apparent

### Inhibition

* Reversibility\_yes
  * type: string
  * description: inhbition type - competitive, uncompetitive, mixed, kic, SE, Unit, Math function
* Reversibility\_no
  * type: string
  * description: ki, SE, Unit, Comment