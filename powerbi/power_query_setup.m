// ==============================================================================
// Power Query M Scripts — Mitron Bank Tableau to Power BI Migration
// Grain & Schema Definitions
// ==============================================================================

// ------------------------------------------------------------------------------
// 1. dim_customers Query
// ------------------------------------------------------------------------------
let
    Source = Csv.Document(File.Contents(File.DirectoryName(#"DatasetPath") & "\Dataset\dim_customers.csv"),[Delimiter=",", Columns=7, Encoding=1252, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"customer_id", type text}, 
        {"age_group", type text}, 
        {"city", type text}, 
        {"occupation", type text}, 
        {"gender", type text}, 
        {"marital status", type text}, 
        {"avg_income", Currency.Type}
    }),
    #"Renamed Columns" = Table.RenameColumns(#"Changed Type",{{"marital status", "marital_status"}})
in
    #"Renamed Columns"

// ------------------------------------------------------------------------------
// 2. fact_spends Query
// ------------------------------------------------------------------------------
let
    Source = Csv.Document(File.Contents(File.DirectoryName(#"DatasetPath") & "\Dataset\fact_spends.csv"),[Delimiter=",", Columns=5, Encoding=1252, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"customer_id", type text}, 
        {"month", type text}, 
        {"category", type text}, 
        {"payment_type", type text}, 
        {"spend", Currency.Type}
    })
in
    #"Changed Type"

// ------------------------------------------------------------------------------
// 3. Dates Dimension (Derived Table M Script or DAX Table)
// ------------------------------------------------------------------------------
let
    Source = Table.SelectColumns(fact_spends, {"month"}),
    #"Removed Duplicates" = Table.Distinct(Source),
    #"Renamed Columns" = Table.RenameColumns(#"Removed Duplicates",{{"month", "MonthName"}}),
    #"Added Custom" = Table.AddColumn(#"Renamed Columns", "month_index", each Date.Month(Date.FromText("01-" & [MonthName] & "-2023")), Int64.Type)
in
    #"Added Custom"
