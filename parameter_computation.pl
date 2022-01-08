#!/usr/bin/perl
use Math::Complex;
$s    = 40000; # Sample rate ( Hz )
$Fc   = shift; # Lowpass filter cut frequency ( Hz )
$Db   = shift; # Level db
$Gd   = -5 * $Db / 6 - 3; # Lowpass filter gain ( dB )
$Ad_h = $Db / 6 - 3; # Highboost filter gain ( dB ) ( 0dB is highs )
$G    = 10 ** ( $Gd / 20 ); $A_h  = 10 ** ( $Ad_h / 20 ); $G_h  = 1 - $A_h;
$Gd_h = 20 * log( $G_h ) / log( 10 );
$Fc_h = $Fc * ( 2 ** ( ( $Gd - $Gd_h ) / 12 ) )/ ( 10 ** ( - $Ad_h / 80 / 0.5 ) );
print "Fc_low = $Fc\nFc_high = $Fc_h\n"; print "Gd = $Gd\nAd_h = $Ad_h\n";
