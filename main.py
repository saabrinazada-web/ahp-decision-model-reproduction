import numpy as np
import sys

sys.path.append('.')

from src.data.pairwise_matrices import CRITERIA_MATRIX, GAJI_MATRIX, KARIR_MATRIX, FASILITAS_MATRIX, LOKASI_MATRIX
from src.core.ahp_calculator import AHPCalculator
from config import CRITERIA_NAMES, ALTERNATIVE_NAMES

def main():
    print("="*60)
    print("AHP REPRODUCTION - PEMILIHAN TEMPAT KERJA")
    print("="*60)
    
    calc = AHPCalculator()
    
    # 1. ANALISIS KRITERIA
    print("\n[1] ANALISIS KRITERIA")
    print("-"*40)
    
    result_kriteria = calc.analyze_matrix(CRITERIA_MATRIX)
    
    for i, nama in enumerate(CRITERIA_NAMES):
        weight = result_kriteria['priority_vector'][i]
        print(f"{nama:10}: {weight:.4f} ({weight*100:.1f}%)")
    
    print(f"CR = {result_kriteria['cr']:.4f}")
    
    # 2. ANALISIS ALTERNATIF
    print("\n[2] ANALISIS ALTERNATIF PER KRITERIA")
    print("-"*40)
    
    matrices = {
        'Gaji': GAJI_MATRIX,
        'Karir': KARIR_MATRIX,
        'Fasilitas': FASILITAS_MATRIX,
        'Lokasi': LOKASI_MATRIX
    }
    
    all_weights = []
    
    for nama_kriteria, matrix in matrices.items():
        print(f"\n--- {nama_kriteria} ---")
        result = calc.analyze_matrix(matrix)
        weights = result['priority_vector']
        all_weights.append(weights)
        
        for i, alt in enumerate(ALTERNATIVE_NAMES):
            print(f"{alt:15}: {weights[i]:.4f}")
    
    # 3. PRIORITAS GLOBAL
    print("\n[3] PRIORITAS GLOBAL")
    print("-"*40)
    
    weights_matrix = np.column_stack(all_weights)
    bobot_kriteria = result_kriteria['priority_vector']
    
    global_scores = weights_matrix @ bobot_kriteria
    
    # Ranking
    ranking = sorted(zip(ALTERNATIVE_NAMES, global_scores), key=lambda x: x[1], reverse=True)
    
    print("\nRANKING AKHIR:")
    for rank, (alt, score) in enumerate(ranking, 1):
        print(f"{rank}. {alt:20}: {score:.4f} ({score*100:.2f}%)")
    
    print("\n" + "="*60)
    print("SELESAI")
    print("="*60)

if __name__ == "__main__":
    main()