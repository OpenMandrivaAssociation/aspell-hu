%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.99.4.2-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Hungarian
%define languagecode hu
%define lc_ctype hu_HU

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.99.4.2.0
Release:       %mkrel 6
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.sourceforge.net/
#Source:	       http://prdownloads.sourceforge.net/wordlist-hu/wordlist-hu-%{src_ver}.tar.bz2
#URL:		   http://wordlist-hu.sourceforge.net
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}
Provides:      spell-%{languagecode}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

#cp doc/README README.%{languagecode}
#chmod 644 README Copyright README.%{languagecode}

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright doc/*
%{_libdir}/aspell-%{aspell_ver}/*


