#!/usr/bin/perl

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


##########################################################################
# Modules
##########################################################################

eval "use LoxBerry::System";
if ( $@ ) {
    use FindBin;
	use lib "$FindBin::Bin/./perllib";
}

use LoxBerry::System;
use LoxBerry::Web;

# Version of this script
our $version = LoxBerry::System::pluginversion();

use CGI::Carp qw(fatalsToBrowser);
use CGI qw/:standard/;
use Config::Simple;
use HTML::Template;
use warnings;
use strict;
no strict "refs"; # we need it for template system and for contructs like ${"skalar".$i} in loops

##########################################################################
# Variables
##########################################################################
our  $cgi = CGI->new;
my  $lang;

##########################################################################
# Read Settings
##########################################################################

 my $datestring = localtime();
 print STDERR "========== LoxBerry Developertools Version $version === ($datestring) =========\n";
 print STDERR "Global variables from LoxBerry::System\n";
 print STDERR "Homedir:     $lbhomedir\n";
 print STDERR "Plugindir:   $lbplugindir\n";
 print STDERR "CGIdir:      $lbcgidir\n";
 print STDERR "HTMLdir:     $lbhtmldir\n";
 print STDERR "Templatedir: $lbtemplatedir\n";
 print STDERR "Datadir:     $lbdatadir\n";
 print STDERR "Logdir:      $lblogdir\n";
 print STDERR "Configdir:   $lbconfigdir\n";

##########################################################################
# Initialize html templates
##########################################################################

# See http://www.perlmonks.org/?node_id=65642
		
##########################################################################
# Print Template
##########################################################################

# Start with HTML header
print $cgi->header(
         -type    =>      'text/html',
         -charset =>      'utf-8'
);

# Get language from GET, POST or System setting (from LoxBerry::Web)
$lang = lblanguage();


LoxBerry::Web::lbheader("Developer Plugin V$version", "http://www.loxwiki.eu:80/x/vICO");

print '<center>';
print '<p>This plugin has nothing to configure in the Web UI.</p>';
print '<p>If you have some cool tweaks that I could integrate, simply let me know!</p>';
print '<p>Please, drop your wishes and issues directly to the <a target="_blank" href="https://github.com/christianTF/LoxBerry-Plugin-Developertools">GitHub issues section</a>.</p>';
print '</center>';

LoxBerry::Web::lbfooter();

exit;
