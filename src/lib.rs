use pyo3::prelude::*;
// use roxmltree::Document;
use std::fs::File;
use std::io::Read;

#[pyfunction]
fn read_xml_file(file_path: &str) -> PyResult<String> {
    let mut file = File::open(file_path)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    Ok(contents)
}

// #[pyfunction]
// fn parse_xml_file(xml_string: &str) -> Result<Document, roxmltree::Error> {
//     let doc = Document::parse(xml_string)?;
//     Ok(doc)
// }

/// A Python module implemented in Rust.
#[pymodule]
fn irspy(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(read_xml_file, m)?)?;
    Ok(())
}
