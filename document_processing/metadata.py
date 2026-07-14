"""
metadata.py
Extracts comprehensive metadata from industrial documents.
Supports PDF, TXT, images, and more.
"""

import os
import mimetypes
from datetime import datetime
from typing import Dict, Any, Optional
import fitz  # PyMuPDF


class MetadataExtractor:
    """
    Extracts file system, document, and content metadata for FactoryBrain AI.
    """
    
    def __init__(self):
        self.supported_pdf = True  # Set to False if PyMuPDF not available

    # ==========================================
    # Basic File Metadata
    # ==========================================
    def get_file_metadata(self, file_path: str) -> Dict[str, Any]:
        """Extract basic file system metadata."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        stats = os.stat(file_path)
        
        return {
            "filename": os.path.basename(file_path),
            "file_path": file_path,
            "extension": os.path.splitext(file_path)[1].lower(),
            "file_size_bytes": stats.st_size,
            "file_size_mb": round(stats.st_size / (1024 * 1024), 3),
            "created_at": datetime.fromtimestamp(stats.st_ctime).isoformat(),
            "modified_at": datetime.fromtimestamp(stats.st_mtime).isoformat(),
            "mime_type": mimetypes.guess_type(file_path)[0] or "unknown",
        }

    # ==========================================
    # PDF-Specific Metadata
    # ==========================================
    def get_pdf_metadata(self, pdf_path: str) -> Dict[str, Any]:
        """Extract metadata from PDF using PyMuPDF."""
        try:
            document = fitz.open(pdf_path)
            metadata = document.metadata or {}
            
            pdf_meta = {
                "pages": len(document),
                "title": metadata.get("title") or "",
                "author": metadata.get("author") or "",
                "subject": metadata.get("subject") or "",
                "keywords": metadata.get("keywords") or "",
                "creator": metadata.get("creator") or "",
                "producer": metadata.get("producer") or "",
                "creation_date": metadata.get("creationDate") or "",
                "modification_date": metadata.get("modDate") or "",
            }
            
            document.close()
            return pdf_meta
            
        except Exception as e:
            return {
                "pages": 0,
                "error": f"Failed to extract PDF metadata: {str(e)}"
            }

    # ==========================================
    # Text Statistics
    # ==========================================
    def get_text_statistics(self, text: str) -> Dict[str, int]:
        """Generate statistics from extracted text."""
        if not text:
            return {"word_count": 0, "character_count": 0, "line_count": 0}
        
        words = text.split()
        return {
            "word_count": len(words),
            "character_count": len(text),
            "line_count": len(text.splitlines()),
            "estimated_reading_time_minutes": round(len(words) / 200, 1),  # Average reading speed
        }

    # ==========================================
    # Main Extraction Method
    # ==========================================
    def extract(self, file_path: str, extracted_text: str = "") -> Dict[str, Any]:
        """
        Extract all available metadata for a document.
        """
        metadata = self.get_file_metadata(file_path)
        
        # Add PDF-specific metadata
        if metadata["extension"] == ".pdf":
            metadata.update(self.get_pdf_metadata(file_path))
        
        # Add text-based statistics
        if extracted_text:
            metadata.update(self.get_text_statistics(extracted_text))
        
        # Add processing timestamp
        metadata["processed_at"] = datetime.now().isoformat()
        metadata["processed_by"] = "FactoryBrain AI MetadataExtractor"
        
        return metadata


# ==========================================
# Demo
# ==========================================
if __name__ == "__main__":
    extractor = MetadataExtractor()
    sample_file = "uploads/sample.pdf"
    
    if os.path.exists(sample_file):
        sample_text = """
        Pump A requires regular maintenance every 500 hours.
        Valve X showed signs of leakage during last inspection.
        Boiler 3 passed all safety compliance checks.
        """
        
        metadata = extractor.extract(sample_file, sample_text)
        
        print("✅ Metadata Extraction Complete\n")
        print("=" * 70)
        
        for key, value in sorted(metadata.items()):
            if isinstance(value, dict):
                print(f"{key}:")
                for k, v in value.items():
                    print(f"   {k}: {v}")
            else:
                print(f"{key:25}: {value}")
    else:
        print("⚠️ Sample file not found. Please add a file to 'uploads/sample.pdf'")
